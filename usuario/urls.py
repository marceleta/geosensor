
from django.urls import path
from .views import *

app_name = 'usuario'

urlpatterns = [
    path('',login_usuario, name='login'),
    path('dashboard/',dashboard, name='dashboard')    
]
