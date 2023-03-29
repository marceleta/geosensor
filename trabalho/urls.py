from django.urls import path
from .views import *

app_name = 'trabalho'
urlpatterns = [
    path('', trabalhos, name='trabalhos'),
    path('recebe-posicoes/', recebe_posicoes, name='recebe_posicoes'),
    path('detalhe/mapa/', mapa, name='mapa'),
    path('detalhe/mapa/json/', mapa_json, name='mapa_json'),
    path('detalhe/json/', trabalhos_ajax, name='json')
    
]