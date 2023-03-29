from trator.models import Trator
from django import forms

class RecebePosicaoForm(forms.Form):

    mac = forms.CharField(label='mac', max_length=17, required=True)
    arquivo = forms.FileField(label='arquivo',required=True)
    md5 = forms.CharField(label='md5', required=True)


class PesquisaTrabalhoForm(forms.Form):

    data = forms.DateField(label='data',required=True) 
    trator = forms.ChoiceField(label='trator', required=True, choices=Trator.lista_tuple())
    h_inicio = forms.TimeField(label='h. início')
    h_final = forms.TimeField(label='h. final')

