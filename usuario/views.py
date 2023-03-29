import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login_usuario(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('usuario:dashboard')
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
        
    
    return render(request, 'login.html', {'form':form})


def dashboard(request):

    return render(request, 'dashboard.html', {})
