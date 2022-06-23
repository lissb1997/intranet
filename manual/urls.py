from django.urls import path
from . import views

# Registrar el espacio de nombres de esta aplicacion
app_name = 'manual'

# Lista con los patrones URL de la aplicacion...
urlpatterns = [
    # Reglas para las paginas de la aplicacion
    path('principal_manual', views.principal, name='principal_manual'),
    # procedimientos
    path('listado_procedimiento', views.listado_procedimiento, name='procedimientos'),
    # circulares
    path('listado_circulares', views.listado_circulares, name='list_circ'),
    # instrucciones
    path('listado_instruc', views.listado_instrucciones, name='list_intruc'),
    # biblioteca
    path('listado_biblioteca', views.listado_bib, name='list_bib'),
    path('resp_busqueda', views.buscar, name='buscar'),
    path(r'^descargar/(?P<file_name>.+)$', views.descargar, name='download'),

]
