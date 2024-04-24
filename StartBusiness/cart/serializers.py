from rest_framework import serializers
from .models import Cart
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user','products']

class CartViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity','products']