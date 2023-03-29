
from django.db import models
from django.db.models import Q
from core.models import ModelTemplate
import json
from trabalho.models import Posicao


class Area(ModelTemplate):
    nome = models.CharField('nome',max_length=100, null=False)
    descricao = models.CharField('descrição',max_length=300, null=True, default='')

    def __str__(self):
        return 'Nome: {}, Descrição: {}'.format(self.nome, self.descricao)

    def ponto_centro(self):
        ponto = Ponto.objects.get(area=self, centro_area=True)
        return ponto.to_dict()

    
    def vertices(self):
        """lista"""
        return list(Ponto.objects.filter(area=self, centro_area=False))

    def _vertices(self):
        """lista dict"""        
        pontos = Ponto.objects.filter(area=self, centro_area=False)
        lista = []
        for ponto in pontos:
            lista.append(ponto.to_dict())
        return lista


    def ruas(self):
        return list(Rua.objects.filter(a_rea=self))

    def _ruas(self):
        ruas = Rua.area(self)
        
        return ruas


    @staticmethod
    def todos():
        return list(Area.objects.all())   


    def to_dict(self):
        d={
            'nome':self.nome,
            'centro':self.ponto_centro(),
            'vertices':self._vertices(),
            'ruas': self._ruas()
                   
            }

        return d


    @staticmethod
    def todos_json():
        areas = Area.objects.all()
        lista = []
        for area in areas:
            lista.append(area.to_dict())

        d = {
            'areas':lista
        }
        
        #print(lista)

        return d
    @staticmethod
    def json(id):
        area = Area.objects.get(pk=id)

        d = {
            'area':area.to_dict()
        }

        return d


    @staticmethod
    def criar(area_json):

        j_areas = json.loads(area_json)

        for a in j_areas['areas']:
            area = Area()
            area.nome = a['nome']
            area.save()           

            centro = Ponto()
            centro.lat = a['centro']['lat']
            centro.lng = a['centro']['lng']
            centro.area = area
            centro.centro_area = True
            centro.save()

            for ver in a['vertices']:
                ponto = Ponto()
                ponto.lat = ver['lat']
                ponto.lng = ver['lng']
                ponto.centro_area = False
                ponto.area = area
                ponto.save()
                
            try:
                
                for r in a['ruas']:
                    rua = Rua()
                    rua.nome = r['nome']
                    rua.a_rea = area
                    rua.save()

                    for p in r['pontos']:
                        ponto = Ponto()
                        ponto.lat = p['lat']
                        ponto.lng = p['lng']
                        ponto.centro_area = False
                        ponto.rua = rua
                        ponto.save()
                        
            except KeyError:
                pass
                

class Rota(ModelTemplate):
    nome = models.CharField('Nome rota', max_length=100, null=False)
    descricao = models.CharField('Descrição', max_length=255, null=True)
    
    def __pesquisa_posicao(self, id_inicio, id_final):
        posicoes = Posicao.objects.filter(Q(pk__gte=id_inicio) & Q(pk__lte=id_final))
        
        return posicoes
    
    
    def criar(self, nome, id_inicio, id_final):
        rota = Rota()
        rota.nome = nome
        rota.save()
        posicoes = self.__pesquisa_posicao(id_inicio, id_final)
        
        for posicao in posicoes:
            ponto = Ponto()
            ponto.lat = posicao.lat
            ponto.lng = posicao.lng
            ponto.rota = rota
            ponto.save()
            
            
    def todos(self):
        return Rota.objects.all()
        
        
    
    def get_pontos(self):
        return Ponto.objects.filter(rota=self)


class Rua(ModelTemplate):
    a_rea = models.ForeignKey(Area,on_delete=models.PROTECT, null=False, default=None)
    nome = models.CharField('nome', max_length=30, null=False)


    def _pontos(self):
        """lista"""
        return list(Ponto.objects.filter(rua=self, centro_area=False))

    
    def pontos(self):
        """Lista dict"""
        pontos = Ponto.objects.filter(rua=self, centro_area=False)
        lista = []
        for ponto in pontos:
            lista.append(ponto.to_dict())

        return lista


    def to_dict(self):
        d = {
            'nome':self.nome,
            'pontos':self.pontos()
        }


    @staticmethod
    def area(area):
        """lista dict"""
        ruas = Rua.objects.filter(a_rea=area)
        lista = []
        for rua in ruas:
            lista.append(rua.to_dict())

        return lista
    

    def to_dict(self):
        d= {
            'nome': self.nome,
            'pontos':self.pontos()
        }

        return d



class Ponto(ModelTemplate):

    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)

    centro_area = models.BooleanField(null=True)

    area = models.ForeignKey(Area, on_delete=models.PROTECT, null=True, default=None)
    rua = models.ForeignKey(Rua, on_delete=models.PROTECT, null=True, default=None)
    rota = models.ForeignKey(Rota, on_delete=models.PROTECT, null=True, default=None)
    

    def to_dict(self):
        return {'lat':self.lat, 'lng':self.lng}

    def to_tuple(self):
        return self.lat, self.lng
    
    


