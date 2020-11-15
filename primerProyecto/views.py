from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime


def index(request):
    # usando cargadores
    plantilla = loader.get_template('template.html')

    contexto = {
        "Nombre": "Santiago",
        "Edad": 25,
        "Fecha": datetime.datetime.now()
    }

    respuesta = plantilla.render(contexto)

    return HttpResponse(respuesta)


def contacto(request):
    plantilla = loader.get_template('template2.html')

    contexto = {
        "Datos_contacto": {
            "Telefono": 11223344,
            "Correo": "santi@gml.com",
            "Direccion": "9 de Julio 9182"
        }
    }

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def about(request):
    plantilla = loader.get_template('template3.html')

    contexto = {

    }
    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def articulos(request):
    contexto = {
        "articulos": {
            1: "Primer articulo",
            2: "Segundo articulo",
            3: "Tercer articulo"
        }
    }

    return render(request, 'template4.html', contexto)
