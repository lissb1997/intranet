from django.shortcuts import render
from .models import Persona, Centro_Externo, OtrosEspacios
from django.http import HttpResponseRedirect, HttpResponseNotFound


# Create your views here.
# ********************* Principal *******************************
def principal(request):
    return render(request, 'directorio/principal_directorio.html')


# ********************** Personal **********************************
def listado_personal(request):
    # creando el contexto
    contexto = {'personal': Persona.objects.all()}
    # devolviendo el contexto
    # hacer html
    return render(request, 'directorio/listado_personal.html', contexto)


def listado_CE(request):
    # creando el contexto
    contexto = {'centro_ext': Centro_Externo.objects.all()}
    # devolviendo el contexto
    return render(request, 'directorio/listado_CE.html', contexto)


def buscar(request):
    contexto = {}
    if request.GET.get('submit'):
        if request:
            contexto['persona'] = Persona.objects.filter(request)
            contexto['centro_ext'] = Centro_Externo.objects.filter(request)
            contexto['otro'] = OtrosEspacios.objects.filter(request)
            return render('directorio/resp_busqueda', contexto)
        else:
            print(
                'Los valores proporcionados no se corresponden con los criterios de búsqueda')
        return render('directorio/resp_busqueda', contexto)
