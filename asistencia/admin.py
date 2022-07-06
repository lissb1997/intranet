from atexit import register
from django.contrib import admin

from .resourse import AsistenciaResource
from .models import Asistencia
from import_export.admin import ImportExportModelAdmin

class AsistenciaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AsistenciaResource

admin.site.register(Asistencia,AsistenciaAdmin)