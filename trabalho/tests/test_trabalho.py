from datetime import datetime
from django.conf import settings
from django.test import TestCase
from trabalho.models import Trabalho
from dispositivo.models import Dispositivo
from core.util import str_to_time

from trator.models import Trator


class TrabalhoTest(TestCase):

    def setUp(self):
        trator = Trator(descricao='descricao', modelo='modelo', ativo=True)
        trator.save()
        self.disp = Dispositivo(mac="c0:18:85:d4:57:51", modelo='modelo', trator=trator)
        self.disp.save()



    def test_trabalho_1_dia(self):
        """Testa se retorna uma lista de posicoes"""
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()

        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")
        resultado = len(lista)
        esperado = 1

        self.assertEqual(resultado, esperado)


    
    def test_trabalho_2_dias(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_2_dias.json', 'r')
        texto = file.read()

        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")
        resultado = len(lista)
        esperado = 2

        self.assertEqual(resultado, esperado)


    def test_trabalho_hora_inicio(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()

        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")
        trabalho = lista[0]
        resultado = trabalho.h_inicio
        d = datetime(2000,1,1,14,0)
        esperado = d.time()

        self.assertEqual(resultado, esperado)


    def test_trabalho_hora_final(self):
        """Testa se retorna uma lista de posicoes"""
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()

        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")
        trabalho = lista[0]
        resultado = trabalho.h_final
        d = datetime(2000,1,1,18,0)
        esperado = d.time()

        self.assertEqual(resultado, esperado)

    def test_trabalho_horas_trabalhadas(self):
       
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()

        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")
        trabalho = lista[0]
        resultado = trabalho.horas_trabalhadas
        
        esperado = 4

        self.assertEqual(resultado.hour, esperado)


    def test_trabalho_maior_velocidade(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()

        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")
        trabalho = lista[0]
        resultado = trabalho.maior_velocidade
        
        esperado = float(12)

        self.assertEqual(resultado, esperado)


    def test_trabalho_velocidade_media(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()

        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")
        trabalho = lista[0]
        resultado = trabalho.velocidade_media
        
        esperado = float(10.40)

        self.assertEqual(resultado, esperado)


    def test_trabalho_duas_entradas_mesmo_dia_velocidade_media(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_mesmo_dia.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        trabalho = lista[0]
        resultado = trabalho.velocidade_media
        
        esperado = float(11.40)

        self.assertEqual(resultado, esperado)

    def test_trabalho_duas_entradas_mesmo_dia_maior_velocidade(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_mesmo_dia.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        trabalho = lista[0]
        resultado = trabalho.maior_velocidade
        
        esperado = float(20)

        self.assertEqual(resultado, esperado)

    
    def test_trabalho_duas_entradas_mesmo_dia_horas_trabalhadas(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_mesmo_dia.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        trabalho = lista[0]
        resultado = trabalho.horas_trabalhadas
        
        esperado = float(9)

        self.assertEqual(resultado.hour, esperado)


    def test_trabalho_duas_entradas_mesmo_dia_horario_inicio(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_mesmo_dia.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        trabalho = lista[0]
        resultado = trabalho.h_inicio
        
        esperado = 14

        self.assertEqual(resultado.hour, esperado)


    def test_trabalho_duas_entradas_mesmo_dia_horario_final(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_mesmo_dia.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        trabalho = lista[0]
        resultado = trabalho.h_final
        
        esperado = 23

        self.assertEqual(resultado.hour, esperado)

    
    def test_trabalho_duas_entradas_mesmo_dia_1_trabalho(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_mesmo_dia.json', 'r')
        texto = file.read()
        Trabalho.criar(texto, "c0:18:85:d4:57:51")

        
        resultado = len(Trabalho.objects.all())
        
        esperado = 1

        self.assertEqual(resultado, esperado)


    def test_trabalho_dias_diferentes(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        Trabalho.criar(texto, "c0:18:85:d4:57:51")

        file = open(settings.MEDIA_ROOT+'/tests/posicoes22022022_teste.json', 'r')
        texto = file.read()
        Trabalho.criar(texto, "c0:18:85:d4:57:51")
        
        resultado = len(Trabalho.objects.all())
        
        esperado = 2

        self.assertEqual(resultado, esperado)



    def test_trabalho_duas_entradas_mesmo_dia_quantidade_de_pontos(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste_mesmo_dia.json', 'r')
        texto = file.read()
        trabalho = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        
        resultado = len(trabalho[0].posicoes())
        
        esperado = 10
        self.assertEqual(resultado, esperado)


    def test_trabalho_pesquisa_json(self):
        
        file = open(settings.MEDIA_ROOT+'/tests/posicoes21022022_teste.json', 'r')
        texto = file.read()
        lista = Trabalho.criar(texto, "c0:18:85:d4:57:51")

        json = Trabalho.json(trabalho=lista[0].pk, h_inicio=str_to_time('14:00'), h_final=str_to_time('14:10'))

        lista = json['trabalho']
        resultado = len(lista)
        esperado = 4

        self.assertEqual(resultado, esperado)





