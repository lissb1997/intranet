from itertools import groupby
from multiprocessing import context
from urllib import request, response
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from directorio.models import Persona
from asistencia.forms import AsistenciaForm
from asistencia.models import Asistencia
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from .resourse import AsistenciaResource


# ****************** Principal************************************
def principal(request):
    return render(request, 'asistencia/principal_asistencia.html')

#


@method_decorator(login_required, name='dispatch')
class AsistenciaListView(ListView):
    model = Asistencia
    template_name = 'asistencia/asistencia_list.html'
    context_object_name = 'asistencia'
    paginate_by = 10

    def get_queryset(self):
        asist_list = Asistencia.objects.filter(usuario=self.request.user)
        return asist_list


@method_decorator(login_required, name='dispatch')
class AsistenciaCreateView(CreateView):
    """View to create a new asistencia"""
    template_name = 'asistencia/asistencia_form.html'
    form_class = AsistenciaForm
    success_url = reverse_lazy('asistencia:list')


@method_decorator(login_required, name='dispatch')
class AsistenciaUpdateView(UpdateView):
    """View to edit a new asistencia"""
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'asistencia/asistencia_form.html'
    success_url = reverse_lazy('asistencia:list')

# ******************** Autorizar *******************************************


def autorizar(request):
    # si estas autenticado y en cargo eres director muestras la asistencia de
    # los subordinados del area y pones en true o false el autorizo de la
    # asistencia
    # el listado debe ser ordenado por trabajador y que se pueda cambiar todos los estados a true o uno a uno

    pass


@method_decorator(login_required, name='dispatch')
class AsistenciaDiasFaltadosListView(ListView):
    model = Asistencia
    template_name = 'asistencia/filtrado.html'
    context_object_name = 'faltas'
    paginate_by = 10

    def get_queryset(self):
        cantidad_dias = Asistencia.objects.filter(
            usuario=self.request.user).count()
        # nombre_Usuario = Persona.objects.filter(usuario=self.request.user)
        # resultado =['cantidad_dias','nombre_Usuario']
        return cantidad_dias

    def get_context_data(self, **kwargs):
        context = {}
        context['Nombre'] = Persona.objects.filter(usuario=self.request.user)
        return context


# @method_decorator(login_required, name='dispatch')

# def export(request):
#     asistencia_resouse = AsistenciaResource()
#     dataset = asistencia_resouse.export()
#     response = HttpResponse(
#         dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="persons.xls"'
#     return response
    