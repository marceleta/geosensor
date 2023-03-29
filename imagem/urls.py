from django.urls import path
from imagem import views

app_name='imagem'

urlpatterns = [
    path('', views.imagens, name='imagens'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('loading/', views.loading, name='loading'),
    path('exibir/<int:id>', views.get_imagem, name='exibir')
]