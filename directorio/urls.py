from . import views
from django.urls import path

# Registrar el espacio de nombres de esta aplicacion
app_name = 'directorio'

# Lista con los patrones URL de la aplicacion...
urlpatterns = [
    # Reglas para las paginas de la aplicacion
    path('principal_directorio', views.principal, name='principal_directorio'),
    # personal
    path('listado_prersonal', views.listado_personal, name='lista_persona'),
    # centro externo
    path('listado_centro_externo', views.listado_CE, name='lista_ce'),
    path('buscar', views.buscar, name='resp_busqueda')

]
