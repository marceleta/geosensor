from django.urls import path
from dispositivo.views import *

app_name='dispositivo'

urlpatterns = [
    path('', dispositivos, name='dispositivos'),
    path('dispositivos/adicionar', adicionar, name='adicionar'),
    path('temperatura', temperatura, name='temperatura')
]