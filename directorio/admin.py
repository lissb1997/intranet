from django.contrib import admin
from .models import Persona, Centro_Externo, OtrosEspacios


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    """describe lo que ve la vista de la administracion con respecto a una persona"""

    list_display = (
        'nombre',
        'apellidos',
        'usuario',
        'area',
        'cargo',
        'ext_telef',
        'telef_dir',
        'correo',
        'cumple',
    )
    list_filter = (
        'nombre',
        'apellidos',
        'usuario',
        'area',
        'cargo',
        'ext_telef',
        'telef_dir',
        'correo',
    )
    search_fields = (
        'nombre',
        'apellidos',
        'area',
        'ext_telef',
        'cargo'
    )
    ordering = ('area', 'nombre')


@admin.register(Centro_Externo)
class CentroExt(admin.ModelAdmin):
    """describe lo que ve la vista de centro externo"""
    list_display = (
        'nombreEntidad',
        'encargado',
        'telefono',
        'direccion',
        'area',
        'categoria',
        'supervisor',

    )
    ordering = ('area', 'nombreEntidad')
    search_fields = ('nombreEntidad', 'area', 'encargado')

@admin.register(OtrosEspacios)
class OtrosEspacios(admin.ModelAdmin):
    list_display = (
        'nombre',
        'telef')
    
