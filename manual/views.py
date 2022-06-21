from django.conf import settings
from django.shortcuts import render

from .filters import BibliotecaFilter, InstrucFilter, ProcedimientoFilter, CircularFilter
from .models import Biblioteca, Circular, Instruc, Procedimiento
from wsgiref.util import FileWrapper
from django.conf import settings
import mimetypes    
from django.http import HttpResponse
import os
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    contexto['filter'] = CircularFilter(
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
    # paginator = Paginator(contexto,10)
    # page_number = request.GET.get('page')
    # var = paginator.get_page(page_number)
    # try:
    #     var = paginator.get_page(page_number)
    # except PageNotAnInteger:
    #     var = paginator.get_page(1)
    # except EmptyPage:
    #     var = paginator.get_page(paginator.num_pages)    
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
   

def descargar(request,archivo):
    file_path = settings.MEDIA_ROOT +'/'+ archivo
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % str(archivo) 
    return response

