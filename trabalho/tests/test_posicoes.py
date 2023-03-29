from django.conf import settings
from django.test import TestCase
from core.util import str_to_time
from trabalho.models import Posicao, Trabalho
from trator.models import Trator
from dispositivo.models import Dispositivo
import json


class PosicaoTest(TestCase):


    def setUp(self):
        trator = Trator(descricao='descricao', modelo='modelo', ativo=True)
        trator.save()
        self.disp = Dispositivo(mac="c0:18:85:d4:57:51", modelo='modelo', trator=trator)
        self.disp.save()

    
    def test_posicoes_1_dia(self):
        """Testa se retorna uma lista de posicoes"""
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        p_json = json.loads(texto)

        lista = Posicao.json_to_objects(p_json['conteudo'])
        resultado = len(lista)
        esperado = 1

        self.assertEqual(resultado, esperado)

    def test_posicoes_tamanho_da_lista(self):
        """verifica se a lista tem a quantidade de posicoes correta"""
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        p_json = json.loads(texto)

        lista = Posicao.json_to_objects(p_json['conteudo'])
        resultado = len(lista[0])
        esperado = 5

        self.assertEqual(resultado, esperado)
    
    def test_posicoes_2_dias(self):
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_2_dias.json', 'r')
        texto = file.read()
        p_json = json.loads(texto)

        lista = Posicao.json_to_objects(p_json['conteudo'])
        resultado = len(lista)
        esperado = 2

        self.assertEqual(resultado, esperado)


    def test_posicoes_pesquisa(self):
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()

        lista  = Trabalho.criar(texto, "c0:18:85:d4:57:51")
        trabalho = lista[0]

        h_inicio = str_to_time('14:00')
        h_final = str_to_time('14:10')

        lista = Posicao.pesquisa(trabalho.pk, h_inicio=h_inicio, h_final=h_final)
        
        resultado = len(lista)
        esperado = 4

        self.assertEqual(resultado, esperado)




