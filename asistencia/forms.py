from django import forms
from .models import Asistencia
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
#from .widgets import *

# Formulario para llenar una asistencia
class AsistenciaForm(forms.ModelForm):

    class Meta:
        model = Asistencia
        fields = ('hora_entrada_M', 'hora_salida_M', 'hora_entrada_T',
                  'hora_salida_T', 'vacaciones_Inicio', 'vacaciones_Fin', 'observaciones',)
        widgets = { 'hora_entrada_T' : TimePickerInput(), 
                   'hora_entrada_M' : TimePickerInput(),
                   'hora_salida_T' : TimePickerInput(),
                   'hora_salida_M' : TimePickerInput(),
                   'observaciones' : forms.Textarea(),
                   'vacaciones_Inicio' : DatePickerInput(format='%d/%m/%Y').start_of('Vacaciones'),
                   'vacaciones_Fin' : DatePickerInput(format='%d/%m/%Y').end_of('Vacaciones'),
                   }
