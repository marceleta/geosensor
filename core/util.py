import datetime
from datetime import timedelta



def diferenca_time(hora_inicio, hora_final):
    h_final = datetime.datetime(2000,1,1,hora_final.hour,hora_final.minute)
    diferenca = timedelta(hours=hora_inicio.hour, minutes=hora_inicio.minute)

    return (h_final - diferenca).time()

def somar_time(hora_inicio, hora_final):
    delta = timedelta(hours=hora_inicio.hour, minutes=hora_inicio.minute)
    h_final = datetime.datetime(2000,1,1,hora_final.hour, hora_final.minute)


    return (h_final + delta).time()


def str_to_date(data):
    date = None
    if data != None:
        if len(data) > 0:
            split = data.split("-")

            ano = split[0]
            mes = split[1]
            dia = split[2]

            if dia[0] == '0':
                dia = int(dia[1])
            if mes[0] == '0':
                mes = int(mes[1])

            date = datetime.datetime(int(ano),int(mes),int(dia)).date()

    return date


def str_to_time(time):
    horario = None
    if time != None:
        if len(time) > 0:
            split = time.split(":")

            hora = split[0]
            minutos = split[1]

            if hora[0] == '0':
                hora = int(hora[1])
            if minutos[0] == '0':
                minutos = int(minutos[1])

            horario = datetime.datetime(2000,1,1, int(hora), int(minutos)).time()

    return horario 




