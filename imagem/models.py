
from django.db import models
from core.models import ModelTemplate

class Imagem(ModelTemplate):
    img = models.ImageField('img')
    nome = models.CharField('nome', max_length=20, null=False, default='')
    north = models.FloatField('north', null=False)
    south = models.FloatField('south', null=False)
    east = models.FloatField('east', null=False)
    west = models.FloatField('west', null=False)



    def __str__(self):
        return self.nome

    def to_dict(self):

        d = {
            'id':self.pk,
            'nome':self.nome,
            'nome':self.nome,
            'north':self.north,
            'south':self.south,
            'east':self.east,
            'west':self.west
        }
        return d

    def to_json():
        lista = []
        for imagem in Imagem.objects.all():
            lista.append(imagem.to_dict())
        return lista


    @staticmethod
    def todos():
        return list(Imagem.objects.all())

