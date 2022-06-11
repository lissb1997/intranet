from django.shortcuts import render

from directorio.models import Persona
from asistencia.forms import AsistenciaForm
from asistencia.models import Asistencia
from django.contrib.auth.models import User
# from .forms import FormCrearAsistencia, FormModifAsistencia
from django.http import HttpResponseRedirect, HttpResponseNotFound


# from django.db.models import F, Q, Count, len
# from datetime import datetime, date

# Create your views here.
# ****************** Principal************************************
def principal(request):
    return render(request, 'asistencia/principal_asistencia.html')


# ********************* listado propio *********************************
def listado_propio(request, self):
    # crando el contexto
    contexto = {}
    if User.is_authenticated:
        contexto['lista'] = Asistencia.objects.filter(usuario=User.get_username(self))
        # devolviendo el contexto
        return render(request, 'asistencia/listado_asistencia_propio.html', contexto)
    else:
        return HttpResponseNotFound("Es necesario que este autenticado en el sistema para acceder a esta sección")


# ************************* Listado General *************************
def listado_asistencia(request):
    # crando el contexto
    contexto = {}
    if User.is_authenticated:
        if User.is_superuser:
            contexto['lista'] = Asistencia.objects.all().order_by('nombre')
            # devolviendo el contexto
            return render(request, 'asistencia/listado_asistencia.html', contexto)  # crear el html
    else:
        return HttpResponseNotFound("Lo sentimos, es necesario estar autenticado")


# *********************** Crear asistencia *******************************
def crear_asistencia(request):
    # Procesando si es post
    if User.is_authenticated:
        if request.method == 'POST':
            # crear la instancia del formulario
            # enlazar los datos usando post
            form = AsistenciaForm(request.POST)
            # verificar si es valido
            if form.is_valid():
                # procesar los datos
                try:
                    print(request.POST)
                except Exception as e:
                    raise e
                # redireccionar a otra pagina para informar que se agregó bien
                # return HttpResponseRedirect("inicio")
        # si es get
        else:
            form = AsistenciaForm()  # lo crea vacío, se va allenar por primera vez
        # creando el contexto
        contexto = {'form': form, 'nombre_formulario': "Registre su Asistencia"}
        return render(request, 'asistencia/crear_asistencia.html', contexto)
    else:
        return HttpResponseNotFound("Debe autenticarse antes")


# ************************* Modificar Asistencia **********************
# def modificar_asistencia(request):
#     if User.is_authenticated:
#         # procesando cuando sea post la solicitud
#         try:
#             asist = Asistencia.objects.get(pk=User.get_username)
#         except Exception as e:
#             print(e.__str__())
#             return HttpResponseNotFound('No existe')
#         if request.method == 'GET':
#             # cra la instancia del formulario pasando el objeto a modificar
#             form = FormModifAsistencia(instance=asist)
#         else:
#             form = FormModifAsistencia(request.POST, instance=asist)
#             if form.is_valid():
#                 # prosesando los datos
#                 try:
#                     form.save()
#                     print(request.POST)
#                 except Exception as e:
#                     raise e
#                 # redireccionar a otra página
#                 return HttpResponseRedirect("principal_asistencia")
#         # creando el contexto
#         contexto = {'form': form, 'id': User.get_username, 'nombre_formulario': "Modificar los datos de su asistencia"}
#         return render(request, 'asistencia/modificar_asistencia.html', contexto)

# ******************* Listar Areas ********************
def listar_personas_por_area(request, area):
    # crando el contexto
    contexto = {}
    if User.is_authenticated:
        if User.is_superuser:
            contexto['lista'] = Persona.objects.filter('area')
            # devolviendo el contexto
            return render(request, 'asistencia/listado_asistencia.html', contexto)  # crear el html
    else:
        return HttpResponseNotFound("Lo sentimos, es necesario estar autenticado")


# ******************** Autorizar *******************************************
def autorizar(request):
    # si estas autenticado y en cargo eres director muestras la asistencia de
    # los subordinados del area y pones en true o false el autorizo de la
    # asistencia
    # el listado debe ser ordenado por trabajador y que se pueda cambiar todos los estados a true o uno a uno

    pass
