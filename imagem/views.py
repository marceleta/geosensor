from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from imagem.forms import ImagemForm
from imagem.models import Imagem

@login_required
def adicionar(request):

    if request.method =='POST':
        form = ImagemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            context = {
                'lista': Imagem.todos(),
                'mensagem':'Imagem salva com sucesso'
            }

            return render(request, 'imagens.html', context)
        else:
            form = ImagemForm()
            return render(request, 'add_imagem.html', {'form':form})

    else:
        form = ImagemForm()
        context = {
            'form':form
        }
        return render(request, 'add_imagem.html', context)

@login_required
def imagens(request):
    imagens = Imagem.todos()
    context = {
        'lista':imagens,
        'mensagem':''
    }

    return render(request, 'imagens.html', context)

@login_required
def loading(request):
    image = open(settings.MEDIA_ROOT+'/loading/loading.gif', 'rb').read()
    return HttpResponse(image, content_type='image/gif')

@login_required
def get_imagem(request, id):
    imagem = Imagem.objects.get(pk=id)
    img = open(imagem.img.path, 'rb').read()
    return HttpResponse(img, content_type='image/png')

