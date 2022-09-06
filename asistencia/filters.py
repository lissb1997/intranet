from dataclasses import field, fields
from pyexpat import model
from re import search
import django_filters

from .models import Asistencia
from directorio.models import Persona
from django.contrib.postgres.search import SearchVector

class AreaFilter(django_filters.FilterSet):
    # search = django_filters.filters.CharFilter(field_name='search', method='filter_search')
    
    class Meta:
        model: Persona
        fields = {
            'area':['exact'],
        }
    # def filter_search(self, queryset, name, value):
    #     search_vector = SearchVector( 'area')
    #     return queryset.annotate(search=search_vector).filter(search__icontains=value)    

class DiasFilter(django_filters.FilterSet):
    # search = django_filters.filters.CharFilter(field_name='search', method='filter_search')
    
    class Meta:
        model: Asistencia
        fields = {
            'usuario':['exact']
        }
    # def filter_search(self, queryset, name, value):
    #     search_vector = SearchVector('usuario')
    #     return queryset.annotate(search=search_vector).filter(search__icontains=value)

