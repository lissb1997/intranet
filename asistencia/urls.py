from django import views
from django.urls import path

from .views import AsistenciaListView, AsistenciaCreateView, AsistenciaUpdateView, AsistenciaDiasFaltadosListView
from . import views

# Registrar el espacio de nombres de esta aplicacion
app_name = 'asistencia'

# Lista con los patrones URL de la aplicacion...
urlpatterns = [
    # Reglas para las paginas de la aplicacion
    path('list', AsistenciaListView.as_view(), name='list'),
    path('create', AsistenciaCreateView.as_view(), name='create'),
    path('update/<int:pk>', AsistenciaUpdateView.as_view(), name='update'),
    #path('autorizar', autorizar, name='autorizar'),
    # path('faltas', views.listado_Faltas, name='faltas')
    path('faltas', AsistenciaDiasFaltadosListView.as_view(), name='faltas'),
    
]
