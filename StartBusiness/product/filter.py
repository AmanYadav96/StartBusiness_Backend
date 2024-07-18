from django_filters import FilterSet
import django_filters
from product.models import Product
from django.db.models import Q
class ProductFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category_name = django_filters.CharFilter(field_name='category__category_name',lookup_expr='icontains')
    brand_name = django_filters.CharFilter(field_name='brand__brand_name',lookup_expr='icontains')
    search = django_filters.CharFilter(method='filter_by_all_fields')
    class Meta:
        model = Product
        fields = ['search','name','status','brand','category','max_price','min_price','category_name','brand_name']

    def filter_by_all_fields(self, queryset, name ,value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(category__category_name__icontains=value) |
            Q(brand__brand_name__icontains=value) 
        )