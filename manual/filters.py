from re import search
import django_filters

from .models import Instruc
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
