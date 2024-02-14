from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Auto
import random
from inicio.forms import FomularioCreacionAuto

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

    
    
    # contexto = Context(dicc)
    # template_renderizado = template.render(dicc)
    # return HttpResponse(template_renderizado)

    return render(request, 'inicio.html', {})

def autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos.html', {'autos': autos})


def mostrar_horario(request):
    fecha = datetime.now()
    return HttpResponse(f'esta es la fecha y hora actual: {fecha}')

def saludo(request, nombre, apellido):
    nombre = nombre.title()
    apellido = apellido.title()
    return HttpResponse(f'Bienvenido {nombre} {apellido}')

# def crear_alumno(request, nombre, apellido, edad):
#     alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad, nota=random.randint(1,10))
#     alumno.save()
#     return render(request,'crear_alumno.html', {'alumno': alumno})

def crear_auto(request):
    # if request.method == "POST":
        # nombre = request.POST.get('nombre')
        # apellido = request.POST.get('apellido')
        # edad = request.POST.get('edad')
        # alumno = Alumno(nombre=nombre, apellido=apellido, edad=edad, nota=random.randint(1,10))
        # alumno.save()
    if request.method == "POST":
        formulario = FomularioCreacionAuto(request.POST)
        if formulario.is_valid():
            patente = formulario.cleaned_data.get('patente')
            marca = formulario.cleaned_data.get('marca')
            ano = formulario.cleaned_data.get('ano')
            nafta=random.randint(1,100)
            auto = Auto(patente=patente, marca=marca, ano=ano, nafta=nafta)
            auto.save()
            return redirect("autos")
            
        
    formulario = FomularioCreacionAuto()
    return render(request,'crear_auto.html', {'formulario': formulario})

    