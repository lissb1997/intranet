from dataclasses import field
from pyexpat import model
from re import search
import django_filters

from .models import Biblioteca, Circular, Instruc, Procedimiento
from django.contrib.postgres.search import SearchVector, SearchQuery


class InstrucFilter(django_filters.FilterSet):
    search = django_filters.filters.CharFilter(field_name='search', method='filter_search')

    class Meta:
        model = Instruc
        fields = {
        #     'tema': ['icontains'],
        #     'anno': ['exact'],
        }
    
    def filter_search(self, queryset, name, value):
        search_vector = SearchVector('titulo', 'anno', 'tema')
        return queryset.annotate(search=search_vector).filter(search__icontains=value)

class ProcedimientoFilter(django_filters.FilterSet):
    search = django_filters.filters.CharFilter(field_name='search', method='filter_search')
    
    class Meta:
        model = Procedimiento
        fields = {
        #     'tema': ['icontains'],
        #     'anno': ['exact'],
        }
    
    def filter_search(self, queryset, name, value):
        search_vector = SearchVector('titulo', 'grupo', 'subGrupo', 'seccion')
        return queryset.annotate(search=search_vector).filter(search__icontains=value)
    
class CircularFilter(django_filters.FilterSet):
    search = django_filters.filters.CharFilter(field_name='search', method='filter_search')
    
    class Meta:
        model = Circular
        fields = {
        #     'tema': ['icontains'],
        #     'anno': ['exact'],
        }
    
    def filter_search(self, queryset, name, value):
        search_vector = SearchVector('titulo', 'organismo', 'anno')
        return queryset.annotate(search=search_vector).filter(search__icontains=value)

class BibliotecaFilter(django_filters.FilterSet):
    search = django_filters.filters.CharFilter(field_name='search', method='filter_search')
    
    class Meta:
        model = Biblioteca
        fields = {
        #     'tema': ['icontains'],
        #     'anno': ['exact'],
        }
    
    def filter_search(self, queryset, name, value):
        search_vector = SearchVector('nombre', 'categoria')
        return queryset.annotate(search=search_vector).filter(search__icontains=value)
