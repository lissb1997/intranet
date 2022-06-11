from django import forms
from .models import Asistencia


# Formulario para llenar una asistencia
class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ('hora_entrada_M', 'hora_salida_M', 'hora_entrada_T', 'hora_salida_T', 'vacaciones', 'observaciones')

    # def __init__(self, *args, **kwargs):
    #     super(FormCrearAsistencia).__init__(*args, **kwargs)
    #     self.fields['hora_entrada_M'].widget.attrs.update(
    #         {'class': 'center', 'placehoulder': 'Title', 'autofocus': 'autofocus'})


# modificar una persona
# class FormModifAsistencia(forms.ModelForm):
#     class Meta:
#         model = Asistencia
#         fields = ('hora_entrada_M', 'hora_salida_M', 'hora_entrada_T', 'hora_salida_T',
#                   'vacaciones', 'observaciones')
