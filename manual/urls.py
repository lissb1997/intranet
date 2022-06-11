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
    # path('crear_procedimiento', views.crear_procedimiento, name='np_submit'),
    # path('modif_procedimiento', views.modificar_procedimiento, name='modif_proced'),
    # path('detalle_procedimiento', views.detalle_procedimiento, name='detalle_proced'),
    # circulares
    path('listado_circulares', views.listado_circulares, name='list_circ'),
    # path('crear_circular', views.crear_circulares, name='np_submit'),
    # path('modif_circular', views.modificar_circular, name='modif_circ'),
    # path('detalle_circular', views.detalle_circular, name='det_circ'),
    # instrucciones
    path('listado_instruc', views.listado_instrucciones, name='list_intruc'),
    # path('crear_instruc', views.crear_instruc, name='np_submit'),
    # path('modif_instruc', views.modificar_instruc, name='modif_instruc'),
    # path('detalle_instruc', views.detalle_instruc, name='det_instruc'),
    # biblioteca
    path('listado_biblioteca', views.listado_bib, name='list_bib'),
    # path('crear_biblio', views.crear_EB, name='crear_EB'),
    # path('modif_biblio', views.modificar_EB, name='modif_bib'),
    # path('detalle_biblio', views.detalle_EB, name='det_bib'),
    path('resp_busqueda', views.buscar, name='buscar'),

]
