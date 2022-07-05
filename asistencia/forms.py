from django import forms
from .models import Asistencia
from .widgets import *

# Formulario para llenar una asistencia
class AsistenciaForm(forms.ModelForm):

    class Meta:
        model = Asistencia
        fields = ('hora_entrada_M', 'hora_salida_M', 'hora_entrada_T',
                  'hora_salida_T', 'observaciones', 'usuario')
        widgets = { 'hora_entrada_T' : TimePickerInput(), 
                   'hora_entrada_M' : TimePickerInput(),
                   'hora_salida_T' : TimePickerInput(),
                   'hora_salida_M' : TimePickerInput(),
                   'vacaciones' : DatePickerInput()}
