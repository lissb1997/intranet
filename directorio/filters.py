from dataclasses import field
from pyexpat import model
from re import search
import django_filters

from .models import Persona, Centro_Externo, OtrosEspacios
from django.contrib.postgres.search import SearchVector

class PersonaFilter(django_filters.FilterSet):
    search = django_filters.filters.CharFilter(field_name='search', method='filter_search')

    class Meta:
        model: Persona
        fields = [
            # 'nombre',
            # 'apellidos',
            # 'area',
            # 'cargo',
            # 'ext_telef',
            # 'telef_dir',
        ]
    def filter_search(self, queryset, name, value):
        search_vector = SearchVector('nombre', 'apellidos', 'area', 'cargo', 'ext_telef', 'telef_dir')
        return queryset.annotate(search=search_vector).filter(search__icontains=value)


class CEFilter(django_filters.FilterSet):
    search = django_filters.filters.CharFilter(field_name='search', method='filter_search')

    class Meta:
        model: Centro_Externo
        fields = {
            # 'nombreEntidad': ['exact'],
            # 'encargado': ['icontains'],
            # 'area': ['exact'],
            # 'categoria': ['exact'],
            # 'supervisor': ['icontains'],
            # 'telefono': ['exact']

        }
    def filter_search(self, queryset, name, value):
        search_vector = SearchVector('nombreEntidad', 'encargado', 'area', 'categoria', 'supervisor', 'telefono')
        return queryset.annotate(search=search_vector).filter(search__icontains=value)

class OtrosEspaciosFilter(django_filters.FilterSet):
    search = django_filters.filters.CharFilter(field_name='search', method='filter_search')

    class Meta:
        model: OtrosEspacios
        fields = {
            
        }
           
    def filter_search(self, queryset, name, value):
        search_vector = SearchVector('nombre',  'telef')
        return queryset.annotate(search=search_vector).filter(search__icontains=value)
