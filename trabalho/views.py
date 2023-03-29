from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from dispositivo.models import Dispositivo
from trator.models import Trator
from area.models import Area
from imagem.models import Imagem
from .models import Trabalho
from .forms import PesquisaTrabalhoForm, RecebePosicaoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import io, zipfile

@login_required
def trabalhos(request):

    form = PesquisaTrabalhoForm()
    lista = Trabalho.todos()
    page = request.GET.get('page',1)

    paginator = Paginator(lista, 10)

    try:
        trabalhos = paginator.page(page)
    except PageNotAnInteger:
        trabalhos = paginator.page(1)
    except EmptyPage:
        trabalhos = paginator.page(paginator.num_pages)

    context = {
        'lista': trabalhos,
        'form': form,
        'h_inicio':'',
        'h_final': ''
    }

    return render(request, 'trabalhos.html', context)

def recebe_posicoes(request):

    if request.method == 'POST':
        form = RecebePosicaoForm(request.POST, request.FILES)
        
        if form.is_valid():
            mac = request.POST['mac']
            query = list(Dispositivo.objects.filter(mac=mac))
            file = request.FILES['arquivo']
            texto = unzip(file.read())
            if texto != None and len(query) > 0:
                Trabalho.criarThread(texto, mac)
                return redirect('trabalho:trabalhos')
            else:
                form = RecebePosicaoForm()
                return render(request, 'receber_arquivo.html',{'form':form})

        else:
            form = RecebePosicaoForm()
            return render(request, 'receber_arquivo.html',{'form':form})
    else:
        form = RecebePosicaoForm()
        return render(request, 'receber_arquivo.html', {'form':form})

@csrf_exempt
@login_required
def mapa_json(request):
    if request.method == "POST":
        h_inicio = request.POST.get('hinicio')
        h_final = request.POST.get('hfinal')
        trabalho = request.POST.get('trabalho')
        zoom = request.POST.get('zoom')
        mapavisivel = request.POST.get('mapavisivel')

        areas = Area.todos_json()
        imagens = Imagem.to_json()
        trabalho = Trabalho.json(trabalho=trabalho, 
                                    h_inicio=h_inicio, h_final=h_final, zoom=zoom,
                                    mapavisivel=mapavisivel)
        context = {
            'trabalho':trabalho,
            'areas': areas['areas'],
            'imagens': imagens
        }
        
        return JsonResponse(context, safe=False)



@login_required
def trabalhos_ajax(request):
    h_inicio = request.GET.get('hinicio')
    h_final =  request.GET.get('hfinal')
    trator = request.GET.get('trator')
    data = request.GET.get('data')

    if trator == '0':
        trabalhos = Trabalho.todos()
    else:
        trabalhos = Trabalho.pesquisa(data, trator, h_inicio, h_final)

    paginator = Paginator(trabalhos, 10)
    lista = paginator.page(1)

    context = {
        'hinicio':h_inicio,
        'hfinal':h_final,
        'lista':lista
    }

    return render(request, 'lista_trabalhos.html', context)


@login_required
def mapa(request):

    return render(request, 'trabalho_mapa.html', {})

def unzip(zipbytes):
    ob = io.BytesIO(zipbytes)
    texto = None
    try:
        with zipfile.ZipFile(ob, mode='r') as zip:
            for z in zip.infolist():
                b = zip.read(z.filename)
                texto = b.decode('utf-8')
    except zipfile.BadZipFile as error:
        pass

    return texto

    