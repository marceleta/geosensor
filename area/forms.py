from django import forms


class AreaForm(forms.Form):
    arquivo = forms.FileField(label='arquivo')
