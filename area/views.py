from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Area, Rota
import json
from .forms import AreaForm
from trabalho.models import Trabalho

@login_required
def areas(request):
    areas = Area.todos()

    context = {
        'lista':areas
    }
    return render(request, 'areas.html', context)

@login_required
def adicionar_arquivo(request):

    if request.method =='POST':
        form = AreaForm(request.POST,request.FILES)
        if form.is_valid():
            file = request.FILES['arquivo']
            Area.criar(file.read())
            return redirect('area:areas')
        else:
            form = AreaForm()
            return render(request, 'add_area.html', {'form':form})
    else:
        form = AreaForm()
        return render(request, 'add_area.html', {'form':form})
    
    
@login_required
def adicionar_mapa(request):
    context = {}
    
    return render(request, 'add_mapa_area.html', context)

@login_required
def areas_json(request):
    areas = Area.todos_json()
    return JsonResponse(areas, safe=False)

def area_json_id(request, id):
    area = Area.json(id)

    return JsonResponse(area, safe=False)    
    

@login_required
def mapa(request):
    return render(request, 'area_mapa.html', {})


@login_required
@csrf_exempt
def salvar_dados_mapa(request):
    
    if request.method == 'POST':
        dados = request.POST.get('areas')
        Area.criar(dados)
        
        context = {
            'sucesso': True
        }
        
        return JsonResponse(context, safe=False)
    
    
@login_required
def selecao_trabalho(request):
    trabalhos = Trabalho.todos()
    page = request.GET.get('page',1)

    paginator = Paginator(trabalhos, 10)

    try:
        trabalhos = paginator.page(page)
    except PageNotAnInteger:
        trabalhos = paginator.page(1)
    except EmptyPage:
        trabalhos = paginator.page(paginator.num_pages)

    context = {
        'lista': trabalhos,
    }

    return render(request, 'trabalho/area_trabalhos.html', context)


@login_required
def criar_nova_rota(request):
    return render(request, 'trabalho/area_mapa_trabalho.html', {})

@login_required
def rota(request):
    rota = Rota()
    
    context = {
        'lista':rota.todos()
    }
    
    return render(request, 'rota.html', context)


@login_required
@csrf_exempt
def recebe_rota_criada(request):
    
    if request.method == 'POST':
        rota = request.POST.get('rota')
        _json = json.loads(rota)
        nome_rota = _json['nome']
        id_inicio = _json['rota'][0]['id']
        id_final = _json['rota'][1]['id']
        rota = Rota()
        rota.criar(nome_rota, id_inicio, id_final)
        
    
    
    return redirect('area:selecao_trabalho')
        
        


