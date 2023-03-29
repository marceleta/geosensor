from django.db import models
from core.models import ModelTemplate
from trator.models import Trator

class Dispositivo(ModelTemplate):
    
    modelo = models.CharField('modelo', max_length=60, null=False, default='')
    mac = models.CharField('mac', max_length=17, null=False, default='')

    trator = models.ForeignKey(Trator, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return "Modelo: {}, Mac: {}".format(self.modelo, self.mac)

    @staticmethod
    def todos():
        return Dispositivo.objects.all()

class Sensor(ModelTemplate):

    temperatura = models.FloatField('temperatura', null=False, default=None)

    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.PROTECT, null=False)

    def salvar(dispostivo, temperatura=None):
        sensor = Sensor()
        sensor.temperatura = temperatura
        sensor.dispositivo = dispostivo
        sensor.save()


    




