from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from dispositivo.models import Dispositivo, Sensor
from .forms import DispoForm, SensorForm

@login_required
def adicionar(request):

    if request.method == 'POST':
        form = DispoForm(request.POST)
        if form.is_valid():
            form.save()

            context = {
                'lista': Dispositivo.todos(),
                'mensagem': 'Dispositivo salvo com sucesso'
            }

            return render(request, 'dispositivos.html', context)
        else:
            form = DispoForm()
    else:
        form = DispoForm()
    
    context = {
        'form':form
    }
    return render(request, 'add_dispositivo.html', context)

@login_required
def dispositivos(request):
    disp = Dispositivo.todos()

    context = {
        'lista': disp,
        'mensagem': ''
    }
    return render(request, 'dispositivos.html', context)


def temperatura(request):
    if request.method == 'POST':
        sensorForm = SensorForm(request.POST)

        if sensorForm.is_valid():
            disp_mac = request.POST['dispositivo']
            temperatura = request.POST['temperatura']
            dispositivo = Dispositivo.objects.get(mac=disp_mac)
            sensor = Sensor()
            sensor.salvar(dispositivo, temperatura=temperatura)
            return redirect('dispositivo:dispositivos')
        else:
            mensagem = 'Os campos abaixo são obrigatórios'
            context = {
                'mensagem':mensagem,
                'form':SensorForm()
            }
            return redirect(request, 'add_sensor.html', context)
    else:
        context = {
            'form':SensorForm()
        }

        return redirect(request, 'add_sensor.html', context)




        
