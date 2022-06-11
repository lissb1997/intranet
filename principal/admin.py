from django.contrib import admin
from django.contrib.admin.models import LogEntry

# Register your models here.
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'
    list_display = (
        'action_time',
        'user',
        'content_type',
        'action_flag',
    )
