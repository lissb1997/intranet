from .models import Asistencia
from import_export import resources


# Register your models here.

class AsistenciaResource(resources.ModelResource):
    class Meta:
        model = Asistencia
        fields = ('fecha_actual', 'nombre', 'hora_entrada_M',
                  'hora_salida_M', 'hora_entrada_T', 'hora_salida_T',
                  'vacaciones_Inicio', 'vacaciones_Fin', 'autorizo',
                  'observaciones')
        export_order = ('fecha_actual', 'nombre', 'hora_entrada_M',
                        'hora_salida_M', 'hora_entrada_T', 'hora_salida_T',
                        'vacaciones_Inicio', 'vacaciones_Fin', 'autorizo',
                        'observaciones')
