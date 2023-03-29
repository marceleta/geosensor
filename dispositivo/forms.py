from dataclasses import field
from django import forms
from .models import Dispositivo, Sensor

class DispoForm(forms.ModelForm):

    class Meta:
        model = Dispositivo
        fields = ['modelo', 'mac', 'trator']

class SensorForm(forms.ModelForm):
    
    class Meta:
        model = Sensor
        fields = ['temperatura', 'dispositivo']