from django.shortcuts import render

from .filters import BibliotecaFilter, InstrucFilter, ProcedimientoFilter
from .models import Biblioteca, Circular, Instruc, Procedimiento

# from django.db.models import F, Q, Count, len
# from datetime import datetime, date

# Create your views here.
##################### Principal ##############################################


def principal(request):
    return render(request, 'manual/principal_manual.html')


########################## procedimientos######################################
def listado_procedimiento(request):
    # crando el contexto
    contexto = {}
    contexto['filter'] = ProcedimientoFilter(
        request.GET, queryset=Procedimiento.objects.all())
    # devolviendo el contexto
    return render(request, 'manual/listado_procedimientos.html', contexto)

##################### Circulares ######################################


def listado_circulares(request):
    # crando el contexto
    contexto = {}
    contexto['filter'] = ProcedimientoFilter(
        request.GET, queryset=Circular.objects.all())
    # devolviendo el contexto
    return render(request, 'manual/listado_circulares.html', contexto)

######################### Instrucciones ###########################


def listado_instrucciones(request):
    # crando el contexto
    contexto = {}
    # contexto['instruc'] = Instruc.objects.all()
    contexto['filter'] = InstrucFilter(
        request.GET, queryset=Instruc.objects.all())
    # devolviendo el contexto
    return render(request, 'manual/listado_instruc.html', contexto)

############################### Biblioteca###################


def listado_bib(request):
    # crando el contexto
    contexto = {}
    contexto['filter'] = BibliotecaFilter(
        request.GET, queryset=Biblioteca.objects.all())
    # devolviendo el contexto
    return render(request, 'manual/listado_biblioteca.html', contexto)


def buscar(request):
    contexto = {}
    if request.GET.get('submit'):
        if request:
            contexto['filter'] = BibliotecaFilter(
                request.GET, queryset=Biblioteca.objects.all())
            contexto['filter'] = InstrucFilter(
        request.GET, queryset=Instruc.objects.all())
            contexto['filter'] = ProcedimientoFilter(
        request.GET, queryset=Circular.objects.all())
            contexto['filter']=ProcedimientoFilter(
        request.GET, queryset = Circular.objects.all())
            return render('manual/resp_busqueda.html', contexto)
        else:
            print(
                'Los valores proporcionados no se corresponden con los criterios de búsqueda')
        return render('manual/resp_busqueda.html', contexto)
