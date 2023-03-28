from django_filters import rest_framework as filters
from reviews.models import Title


class TitleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(lookup_expr='slug')
    category = filters.CharFilter(lookup_expr='slug')

    class Meta:
        model = Title
        fields = ['genre', 'category', 'name', 'year']
