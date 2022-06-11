from django.shortcuts import render


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
    contexto['procedimientos'] = Procedimiento.objects.all()
    # devolviendo el contexto
    return render(request, 'manual/listado_procedimientos.html', contexto)

##################### Circulares ######################################
def listado_circulares(request):
    # crando el contexto
    contexto = {}
    contexto['circulares'] = Circular.objects.all()
    # devolviendo el contexto
    return render(request, 'manual/listado_circulares.html', contexto)

######################### Instrucciones ###########################
def listado_instrucciones(request):
    # crando el contexto
    contexto = {}
    contexto['instruc'] = Instruc.objects.all()
    # devolviendo el contexto
    return render(request, 'manual/listado_instruc.html', contexto)

############################### Biblioteca###################
def listado_bib(request):
    # crando el contexto
    contexto = {}
    contexto['biblioteca'] = Biblioteca.objects.all()
    # devolviendo el contexto
    return render(request, 'manual/listado_biblioteca.html', contexto)

def buscar(request):
    contexto = {}
    if request.GET.get('submit'):
        if request:
            contexto['biblioteca'] = Biblioteca.objects.filter(request)
            contexto['instruc'] = Instruc.objects.filter(request)
            contexto['circular'] = Circular.objects.filter(request)
            contexto['proced'] = Procedimiento.objects.filter(request)
            return render('resp_busqueda', contexto)
        else:
            print('Los valores proporcionados no se corresponden con los criterios de búsqueda')
        return render('resp_busqueda', contexto)
