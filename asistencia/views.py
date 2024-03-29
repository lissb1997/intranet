from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from directorio.models import Persona
from .forms import AsistenciaForm
from .models import Asistencia
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from .filters import AreaFilter, DiasFilter





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

@method_decorator(login_required, name='dispatch')
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

    def get_queryset(request):
        #  creando el contexto
        contexto = {}
        contexto['filter'] = AreaFilter(
            request.GET, queryset=Persona.objects.all())
        for a in contexto.get("usuario"):
            contexto['cant_dias'] = DiasFilter(
                queryset=Asistencia.objects.filter(a))
            contexto['nombre'] = Persona.objects.filter(
                a.usuario).get('nombre', 'apellidos')
            contexto['faltas'] = 24 - len(contexto['cant_dias'])
        return contexto
    
@method_decorator(login_required, name='dispatch')
def listado_Faltas(request):
    # creando el contexto
    # contexto = {}
    # contexto['filter'] = AreaFilter(request.GET, queryset=Persona.objects.all())
    # for a in contexto.get("usuario"):
    #     contexto['cant_dias']=DiasFilter(queryset=Asistencia.objects.filter(a))
    #     contexto['nombre']= Persona.objects.filter(a.usuario).get('nombre', 'apellidos')
    #     contexto['faltas']= 24 - len(contexto['cant_dias'])
    return render(request, 'asistencia/filtrado.html')


# @method_decorator(login_required, name='dispatch')

# def export(request):
#     asistencia_resouse = AsistenciaResource()
#     dataset = asistencia_resouse.export()
#     response = HttpResponse(
#         dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="persons.xls"'
#     return response
