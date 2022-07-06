from django.urls import path

from asistencia import views

# Registrar el espacio de nombres de esta aplicacion
app_name = 'asistencia'

# Lista con los patrones URL de la aplicacion...
urlpatterns = [
    # Reglas para las paginas de la aplicacion
    path('list', views.AsistenciaListView.as_view(), name='list'),
    path('create', views.AsistenciaCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.AsistenciaUpdateView.as_view(), name='update'),
    path('autorizar', views.autorizar, name='autorizar'),
    path('faltados', views.AsistenciaDiasFaltadosListView.as_view(), name='faltados')
]
