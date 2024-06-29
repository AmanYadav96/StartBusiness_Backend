from django_filters import FilterSet
from category.models import Category
import django_filters
class CategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='subcategories__category')
    class Meta:
        model = Category
        fields = ['is_active','category']