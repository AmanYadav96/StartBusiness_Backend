from rest_framework import serializers
from .models import OrderItem,Order
from django.db import transaction
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'address','items','total_price','order_status','created_at','payment_info']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        with transaction.atomic():
            order = Order.objects.create(**validated_data)
            order_items = [OrderItem(order=order, **item_data) for item_data in items_data]
            OrderItem.objects.bulk_create(order_items)
        return order
    



    
