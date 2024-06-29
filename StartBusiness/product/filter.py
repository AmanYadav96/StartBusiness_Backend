from django_filters import FilterSet
import django_filters
from product.models import Product

class ProductFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name','status','brand','category']

