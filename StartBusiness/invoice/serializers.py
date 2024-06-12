from rest_framework import serializers
from invoice.models import Invoice

from rest_framework import serializers
from .models import InvoiceItem,Invoice
from django.db import transaction
class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True)
    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        with transaction.atomic():
            invoice = Invoice.objects.create(**validated_data)
            invoice_items = [InvoiceItem(invoice=invoice, **item_data) for item_data in items_data]
            InvoiceItem.objects.bulk_create(invoice_items)
        return invoice
    

