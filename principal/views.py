from django.shortcuts import render, loader
from django.http import HttpResponse
from datetime import date, datetime, time


def principal_index(request):
    # Creando el contexto
    contexto = {}

    # Devolviendo el documento final al usuario
    return render(request, 'index.html', contexto)
