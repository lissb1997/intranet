from django.contrib import admin
from .models import Biblioteca, Instruc, Procedimiento, Circular


# Register your models here.
@admin.register(Biblioteca)
class Biblioteca(admin.ModelAdmin):
    """Admin View para el modelo biblioteca"""

    list_display = (
        'nombre',
        'categoria',
    )
    
    list_filter = (
        'nombre',
        'categoria',
    )


@admin.register(Instruc)
class Instruc(admin.ModelAdmin):
    """Admin View para el modelo instrucciones"""

    list_display = (
        'tipo',
        'archivo',
        'anno',
        'numero',
        'descripcion',
        'anexo',
        'archivo',
        'tema',

    )
    list_filter = (
        'anno',
        'tema',

    )


@admin.register(Procedimiento)
class Procedimiento(admin.ModelAdmin):
    """Admin View para el modelo procedimientos"""

    list_display = (
        'seccion',
        'grupo',
        'subGrupo',
        'titulo',
        'proforma',
        'anexo',
        'descripcion',
        'archivo',

    )
    list_filter = (
        'titulo',
        'grupo',
        'subGrupo',
        'seccion',
    )


@admin.register(Circular)
class Circular(admin.ModelAdmin):
    """admin view para las circulares"""

    list_display = (
        'anno',
        'numero',
        'organismo',
        'titulo',
        'archivo',
    )

    list_filter = (
        'anno',
        'numero',
        'organismo',
        'titulo',
    )
# Register your models here.

"""class ProcedimientoRecourse(resources.ModelResource):
    class Meta:
        model = Procedimiento

class InstrucRecourse(resources.ModelResource):
    class Meta:
        model = Instruc

class CirRecourse(resources.ModelResource):
    class Meta:
        model = Circular
"""