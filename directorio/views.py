from django.shortcuts import render

from .filters import OtrosEspaciosFilter, PersonaFilter, CEFilter
from .models import Persona, Centro_Externo, OtrosEspacios
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.postgres.search import SearchVector


# Create your views here.
# ********************* Principal *******************************
def principal(request):
    return render(request, 'directorio/principal_directorio.html')


# ********************** Personal **********************************
def listado_personal(request):
    # creando el contexto
    contexto = {}
    contexto['filter'] = PersonaFilter(request.GET, queryset=Persona.objects.all())
    # devolviendo el contexto
    return render(request, 'directorio/listado_personal.html', contexto)


def listado_CE(request):
    # creando el contexto
    contexto = {}
    contexto['filter'] = CEFilter(request.GET, queryset=Centro_Externo.objects.all())
    # devolviendo el contexto
    return render(request, 'directorio/listado_CE.html', contexto)

def listado_OtrosEspacios(request):
    # creando el contexto
    contexto = {}
    contexto['filter'] = OtrosEspaciosFilter(request.GET, queryset=OtrosEspacios.objects.all())
    # devolviendo el contexto
    return render(request, 'directorio/resp_busqueda.html', contexto)


def buscar(request):
    contexto = {}
    if request.GET.get('submit'):
        if request:
            if listado_personal(request).exists():
                return render('directorio/listado_personal.html', contexto)
            if listado_CE(request).exists():
                return render('directorio/listado_CE.html', contexto)
            if listado_OtrosEspacios(request).exists():
                return render('directorio/principal_directorio.html', contexto)
        else:
            print(
                'Los valores proporcionados no se corresponden con los criterios de búsqueda')
        return render('directorio/principal_directorio.html', contexto)
