from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TratorForm
from .models import Trator


@login_required
def adicionar(request):

    if request.method == 'POST' and request.FILES['imagem']:
        
        tratorForm = TratorForm(request.POST, request.FILES)

        if tratorForm.is_valid():
            tratorForm.save()

            mensagem = 'Trator salvo com sucesso'

            context = {
                'lista':Trator.todos(),
                'mensagem': mensagem
            }
            
            return render(request, 'tratores.html', context)
    else:
        form = TratorForm()
        context = {
            'form':form
        }
    return render(request, 'add_trator.html', context)
    

@login_required
def tratores(request):

    context = {
        'lista':Trator.todos(),
        'mensagem':''
    }

    return render(request, 'tratores.html', context)

