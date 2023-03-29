from distutils.command.upload import upload
from django.db import models
from core.models import ModelTemplate

# Create your models here.

class Trator(ModelTemplate):
    imagem = models.ImageField('imagem')
    descricao = models.CharField('descrição', max_length=100, null=True)
    modelo = models.CharField('modelo', max_length=100, null=True)
    ativo = models.BooleanField('ativo', default=True)

    @staticmethod
    def todos():
        return Trator.objects.all()

    @staticmethod
    def lista_tuple():
        tratores = Trator.objects.all()
        lista = []
        for trator in tratores:
            lista.append((trator.pk, trator.descricao))

        return lista


    def __str__(self):
        return self.descricao
