from django import http
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo (request):
    return HttpResponse("Hola Joni - Coder")

def segundaVista(request):
    return HttpResponse("<b>---------YA SOMOS PROGRAMADORES------<b>")

def dia(request):
    variable = datetime.now()
    return HttpResponse(f"HOY ES UN GRAN DIA<br>{variable}")

def apellido(request, ape):
    fecha = datetime.now()
    return HttpResponse(f"<b>Jonatan {ape}, es un capo<b>...<br><br>...Por lo menos hoy: {fecha}")

def probandoTemplate(request):
    miHTML = open("D:/Jonatan-PC/Python/Proyecto23850/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)