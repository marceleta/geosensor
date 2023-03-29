from django import forms
from imagem.models import Imagem

class ImagemForm(forms.ModelForm):

    class Meta:
        model = Imagem
        fields = ['img', 'nome', 'north', 'south', 'east', 'west']