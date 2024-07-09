from django_filters import FilterSet
import django_filters
from product.models import Product

class ProductFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category_name = django_filters.CharFilter(field_name='category__category_name',lookup_expr='icontains')
    brand_name = django_filters.CharFilter(field_name='brand__brand_name',lookup_expr='icontains') 
    class Meta:
        model = Product
        fields = ['name','status','brand','category','max_price','min_price','category_name','brand_name']

