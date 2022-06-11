from django import forms
from .models import Persona, Centro_Externo

# Crear el formulario para crear una persona
class Form_Crear_Personal(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

# modificar una persona
class Form_Modif_Personal(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'


class Form_Crear_CE(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

# modificar una persona
class Form_Modif_CE(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'