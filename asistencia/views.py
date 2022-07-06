from itertools import groupby
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
from django.http import HttpResponseRedirect, HttpResponseNotFound


# ****************** Principal************************************
def principal(request):
    return render(request, 'asistencia/principal_asistencia.html')

# 
@method_decorator(login_required, name='dispatch')
class AsistenciaListView(ListView):
    model = Asistencia
    template_name = 'asistencia/asistencia_list.html'
    context_object_name = 'asistencia'
    paginate_by = 1
    
    def get_queryset(self):
        asist_list = Asistencia.objects.filter(usuario= self.request.user)
        return asist_list
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(AsistenciaListView, self).dispatch(*args, **kwargs)
    
@method_decorator(login_required, name='dispatch')
class AsistenciaCreateView(CreateView):
    """View to create a new asistencia"""
    template_name = 'asistencia/asistencia_form.html'
    form_class = AsistenciaForm
    success_url = reverse_lazy('asistencia:list')
    
@method_decorator(login_required, name='dispatch')
class AsistenciaUpdateView(UpdateView):
    """View to edit a new asistencia"""
    model= Asistencia
    form_class = AsistenciaForm
    template_name = 'asistencia/asistencia_form.html'
    success_url = reverse_lazy('asistencia:list')

# ******************* Listar Areas ********************
def listar_personas_por_area(request, area):
    # crando el contexto
    contexto = {}
    if User.is_authenticated:
        if User.is_superuser:
            contexto['lista'] = Persona.objects.filter('area')
            # devolviendo el contexto
            # crear el html
            return render(request, 'asistencia/listado_asistencia.html', contexto)
    else:
        return HttpResponseNotFound("Lo sentimos, es necesario estar autenticado")


# ******************** Autorizar *******************************************
def autorizar(request):
    # si estas autenticado y en cargo eres director muestras la asistencia de
    # los subordinados del area y pones en true o false el autorizo de la
    # asistencia
    # el listado debe ser ordenado por trabajador y que se pueda cambiar todos los estados a true o uno a uno

    pass
@method_decorator(login_required, name='dispatch')
class AsistenciaInvListView(ListView):
    model = Asistencia
    template_name = 'asistencia/asistencia_list.html'
    context_object_name = 'asistencia'
    paginate_by = 10
    
    def get_queryset(self):
        asist_list = Asistencia.objects.filter(usuario=Asistencia.usuario)
        ordenado = asist_list.order_by(cargo=Persona.area)
        return asist_list
    
