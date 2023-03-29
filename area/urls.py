from django.urls import path
from area.views import *

app_name = 'area'

urlpatterns = [
    path('', areas, name='areas'),    
    path('adicionar/arquivo', adicionar_arquivo, name='adicionar_arquivo'),
    path('adicionar/mapa', adicionar_mapa, name='adicionar_mapa'),
    path('adicionar/mapa/salvar', salvar_dados_mapa, name='salvar_dados_mapa'),    
    path('mapa', mapa, name='mapa'),
    path('mapa/json', areas_json, name='json'),
    path('mapa/json/<int:id>', area_json_id, name='json_id'),
    path('rota', rota, name='area_rota'),
    path('rota/trabalho', selecao_trabalho, name='selecao_trabalho'),
    path('rota/mapa/', criar_nova_rota, name='criar_nova_rota'),
    path('rota/adicionar', recebe_rota_criada, name='recebe_rota_criada')
]