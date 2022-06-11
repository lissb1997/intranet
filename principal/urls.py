from django.urls import path
from . import views

# Lista con los patrones URL de la aplicacion...
urlpatterns = [
    path('', views.principal_index, name='inicio'),
]

