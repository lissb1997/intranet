from django.urls import path

from asistencia import views

# Registrar el espacio de nombres de esta aplicacion
app_name = 'asistencia'

# Lista con los patrones URL de la aplicacion...
urlpatterns = [
    # Reglas para las paginas de la aplicacion
    path('principal_asistencia', views.principal, name='principal_asistencia'),
    path('listado_propio', views.listado_propio, name='listado_propio'),
    path('listado_asistencia', views.listado_asistencia, name='listado_asistencia'),
    path('crear_asistencia', views.crear_asistencia, name='crear_asistencia'),
    # path('modificar_asistencia', views.modificar_asistencia, name='modificar_asistencia'),
    path('autorizar', views.autorizar, name='autorizar')
]
