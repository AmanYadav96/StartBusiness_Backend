from django_filters import FilterSet
from invoice.models import Invoice
import django_filters


class InvoiceFilter(FilterSet):
    class Meta:
        model = Invoice
        fields = ['invoice_status']