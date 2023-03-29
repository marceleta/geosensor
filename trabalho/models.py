from django.db.models import F
from datetime import datetime, timedelta
from django.db import models
from django.db.models import Q
from core.models import ModelTemplate
from dispositivo.models import Dispositivo
from trator.models import Trator
from trabalho.mapa import Mapa
from trabalho.geometria import Geometry
from core.util import str_to_date, str_to_time, diferenca_time, somar_time
import threading
import json

class Trabalho(ModelTemplate):
    data = models.DateField('data', null=False, default=None)
    h_inicio = models.TimeField('hora inicio', null=False)
    h_final = models.TimeField('hora final', null=False)
    horas_trabalhadas = models.TimeField('horas trabalhadas', null=False)
    maior_velocidade = models.FloatField('maior velocidade', null=False)
    velocidade_media = models.FloatField('velocidade media', null=False)

    def __str__(self):
        return "Data: {}, H. início {}, H. final: {}".format(self.data, self.h_inicio, self.h_final)

    @staticmethod
    def todos():
        return Trabalho.objects.all().order_by('data')


    @staticmethod
    def criarThread(json_posicoes, dispositivo):
        thread = threading.Thread(target=Trabalho.__criar, args=[json_posicoes, dispositivo])
        thread.start()


    @staticmethod
    def criar(json_posicoes, dispositivo):
        json_posicoes = json.loads(json_posicoes)
        dispositivo = Dispositivo.objects.get(mac=dispositivo)
        lista_posicoes = Posicao.json_to_objects(json_posicoes['conteudo'])
        trabalhos = []

        for posicoes in lista_posicoes:

            maior_velocidade = 0
            soma_velocidades = 0

            for p in posicoes:
                if maior_velocidade < p.velocidade:
                    maior_velocidade = p.velocidade
                soma_velocidades = soma_velocidades + p.velocidade

            velocidade_media = (soma_velocidades / len(posicoes))

            data = posicoes[0].data_hora.date()
            query = Trabalho.objects.filter(data=data)

            trabalho = None
            for t in query:
                if dispositivo == t.dispositivo():
                    trabalho = t

            if trabalho == None:
                trabalho = Trabalho()
                trabalho.data = posicoes[0].data_hora.date()
                trabalho.h_inicio = posicoes[0].data_hora.time()
                trabalho.h_final = posicoes[-1].data_hora.time()
                trabalho.horas_trabalhadas = diferenca_time(posicoes[0].data_hora.time(), posicoes[-1].data_hora.time())
                trabalho.maior_velocidade = maior_velocidade
                trabalho.velocidade_media = velocidade_media
                trabalho.save()
                trabalhos.append(trabalho)

            else:
                trabalho.h_final = posicoes[-1].data_hora.time()
                trabalho.horas_trabalhadas = diferenca_time(trabalho.h_inicio, trabalho.h_final)
                if trabalho.maior_velocidade < maior_velocidade:
                    trabalho.maior_velocidade = maior_velocidade
                trabalho.velocidade_media = (trabalho.velocidade_media + velocidade_media) / 2
                trabalho.save()
                trabalhos.append(trabalho)

            
            for posicao in posicoes:
                posicao.trabalho = trabalho
                posicao.dispositivo = dispositivo

            Posicao.objects.bulk_create(posicoes)

        return trabalhos



    def dispositivo(self):
        return self.posicoes()[0].dispositivo

    def trator(self):
        return self.posicoes()[0].dispositivo.trator

    def posicoes(self):
        return Posicao.objects.filter(trabalho=self)

    @staticmethod
    def pesquisa(data, trator, h_inicio, h_final):
  
        data = str_to_date(data)

        query = Trabalho.objects.filter(data=data)
        trator = Trator.objects.get(pk=trator)

        trabalhos = []

        for trabalho in query:
            if trator == trabalho.trator():
                q = None
                if h_inicio != '' and h_final != '':
                    horario_inicio = str_to_time(h_inicio)
                    horario_final = str_to_time(h_final)
                    q = Posicao.pesquisa(h_inicio=horario_inicio, h_final=horario_final, trabalho=trabalho)
                    if len(q) > 0:
                        trabalhos.append(trabalho)
                    
                elif h_inicio != '':
                    horario_inicio = str_to_time(h_inicio)
                    q = Posicao.pesquisa(horario_inicio=horario_inicio, trabalho=trabalho)
                    if len(q) > 0:
                        trabalhos.append(trabalho)
                else:
                    trabalhos.append(trabalho)

        return trabalhos
                
    @staticmethod
    def json(trabalho, h_inicio, h_final, zoom, mapavisivel):

        hinicio = str_to_time(h_inicio)
        hfinal = str_to_time(h_final)
        trabalho = Trabalho.objects.get(pk=trabalho)
        posicoes = Posicao.pesquisa_zoom(trabalho=trabalho,zoom=Mapa.zoom(zoom), h_inicio=hinicio, h_final=hfinal)
       
        posicoes_area = Geometry.pontos_na_area(mapavisivel,posicoes)

        return posicoes_area




class Posicao(ModelTemplate):
    
    data_hora = models.DateTimeField('data/hora', null=False)
    lat = models.FloatField('latitude', null=False)
    lng = models.FloatField('longitude', null=False)
    pressao_a = models.FloatField('pressao a', null=False)
    pressao_b = models.FloatField('pressao b', null=False)
    fluxo_a = models.FloatField('fluxo a', null=False)
    fluxo_b = models.FloatField('fluxo b', null=False)
    razao = models.IntegerField('razao', null=False)
    sentido = models.FloatField('sentido', null=False)
    velocidade = models.FloatField('velocidade', null=False)

    trabalho = models.ForeignKey(Trabalho, null=False, on_delete=models.PROTECT)
    dispositivo = models.ForeignKey(Dispositivo, null=False, on_delete=models.PROTECT)


    def __str__(self):
        return "Data: {}, Lat: {}, Lng: {}".format(self.data_hora, self.lat, self.lng)


    def to_dict(self):
        d = {
            'id':self.id,
            'lat':self.lat,
            'lng':self.lng,
            'velocidade':self.velocidade,
            'horario':str(self.data_hora.time())
        }
        return d

    def to_tuple(self):

        return self.lat, self.lng

    def to_popup(self):
        s = '<h5>Horário: {}</h5><p><h5>Velocidade: {}</h5>'.format(str(self.data_hora.time()), str(self.velocidade))

        return s

    @staticmethod
    def json_to_objects(posicoes_json):
        posicoes = Posicao.__json_to_objects(posicoes_json)

        loop = True
        lista = []
        index = 0
        tamanho = (len(posicoes) -1)
        while(loop):
            temp = []
            __loop = True
            while(__loop):
                if posicoes[index].data_hora.date() == posicoes[index+1].data_hora.date():
                    temp.append(posicoes[index])
                else:
                    temp.append(posicoes[index])
                    lista.append(temp)
                    __loop = False
                index = index + 1
                if index == tamanho:
                    temp.append(posicoes[index])
                    lista.append(temp)
                    __loop = False
                    loop = False

        return lista


    @staticmethod
    def __json_to_objects(posicoes_json):

        lista = []
        delta = timedelta(hours=3, minutes=0)
        for p in posicoes_json:
            posicao = Posicao()
            posicao.data_hora = datetime.fromisoformat(p['data_hora']) + delta
            posicao.lat = float(p['lat'])
            posicao.lng = float(p['lng'])
            posicao.pressao_a = float(p['pressao_a'])
            posicao.pressao_b = float(p['pressao_b'])
            posicao.fluxo_a = float(p['fluxo_a'])
            posicao.fluxo_b = float(p['fluxo_a'])
            posicao.razao = int(p['razao'])
            posicao.sentido = float(p['sentido'])
            posicao.velocidade = float(p['velocidade'])

            lista.append(posicao)

        return lista

    @staticmethod
    def pesquisa(trabalho, h_inicio=None, h_final=None):
        
        query = Posicao.objects.filter(trabalho=trabalho)

        if h_inicio != None and h_final != None:
            query = query.filter(Q(data_hora__time__gte=h_inicio) & Q(data_hora__time__lte=h_final))
        elif h_inicio != None:
            query = query.filter(data_hora__time__gte=h_inicio)


        
        return query

    
    @staticmethod
    def pesquisa_zoom(trabalho, zoom, h_inicio=None, h_final=None):
        
        query = Posicao.pesquisa(trabalho=trabalho, h_inicio=h_inicio, h_final=h_final)
        query = query.annotate(id_mod=F('id') % zoom).filter(id_mod=0)

        
        return query
            


        