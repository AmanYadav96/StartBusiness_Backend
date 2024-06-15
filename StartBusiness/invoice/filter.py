from django_filters import FilterSet
from invoice.models import Invoice
import django_filters


class InvoiceFilter(FilterSet):
    customer_name = django_filters.CharFilter(field_name='customer_name', lookup_expr='icontains')
    class Meta:
        model = Invoice
        fields = ['invoice_status','customer_name']