from django.urls import path
from .views import *

app_name = 'trator'
urlpatterns = [
    path('', tratores, name='tratores'),
    path('tratores/adicionar', adicionar, name='adicionar')
]