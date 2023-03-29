from django import forms
from .models import Trator

class TratorForm(forms.ModelForm):

    class Meta:
        model = Trator
        fields = ['imagem', 'descricao', 'modelo']