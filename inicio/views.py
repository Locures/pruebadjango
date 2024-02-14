from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.
def inicio(request):
    # archivo_abierto = open(r'C:\Users\Hogar\Desktop\practica django\inicio\templetes\inicio.html','r')
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    # dicc ={
    #     'nombre': 'Carlos',
    #     'apellido' : 'Perez'
    # }
    # contexto = Context(dicc)
    # template_renderizado = template.render(contexto)
    # return HttpResponse(template_renderizado)

    # template = loader.get_template('inicio.html')

    
    dicc ={
        'nombre': 'Carlos',
        'apellido' : 'Perez'
    }
    # contexto = Context(dicc)
    # template_renderizado = template.render(dicc)
    # return HttpResponse(template_renderizado)

    return render(request, 'inicio.html', dicc)

def mostrar_horario(request):
    fecha = datetime.now()
    return HttpResponse(f'esta es la fecha y hora actual: {fecha}')

def saludo(request, nombre, apellido):
    nombre = nombre.title()
    apellido = apellido.title()
    return HttpResponse(f'Bienvenido {nombre} {apellido}')

    