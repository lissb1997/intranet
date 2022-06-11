from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
  """Admin View para el modelo asistencia"""
  
  list_display = (
    'nombre',
    'hora_entrada_M',
    'hora_salida_M',
    'hora_entrada_T',
    'hora_salida_T',
  )
