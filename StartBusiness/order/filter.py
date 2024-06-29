from django_filters import FilterSet
import django_filters
from order.models import Order
from django_filters import rest_framework as filters

class StatusFilter(filters.BaseInFilter):
    lookup_type = filters.MultipleChoiceFilter
    choices = (('Pending', 'Pending'), ('Placed', 'Placed'),('Cancelled', 'Cancelled'),('Completed', 'Completed')) 

    def filter_queryset(self, queryset, value):
        if value:
            return queryset.filter(order_status__in=value)
        return queryset  


class OrderFilter(FilterSet):
    order_status = StatusFilter()
    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    class Meta:
        model = Order
        fields = ['user','order_status','created_at']