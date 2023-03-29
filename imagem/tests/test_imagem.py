from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse as r
from django.test.client import Client

class ImagemTest(TestCase):


    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test','test@email.com', 'test')

    def test_template_correto_imagens(self):
        self.client.login(username='test', password='test')
        response = self.client.get(r('imagem:imagens'))

        self.assertTemplateUsed(response, 'imagens.html')


    def test_template_correto_imagem(self):
        self.client.login(username='test', password='test')
        response = self.client.get(r('imagem:adicionar'))

        self.assertTemplateUsed(response, 'add_imagem.html')

    def test_criar_imagem(self):
        self.client.login(username='test', password='test')
        file_imagem = open(settings.MEDIA_ROOT+'/tests/DJI_0641_rotacionada16g.png', 'rb')
        
        data = {
            'img':file_imagem,
            'nome':'Area 1',
            'north':1.0,
            'south':1.0,
            'east':1.0,
            'west':1.0
        }
        
        response = self.client.post(r('imagem:adicionar'), data)

        self.assertEqual(response.status_code, 302)


    


