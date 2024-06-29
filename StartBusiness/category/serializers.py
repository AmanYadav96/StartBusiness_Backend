from rest_framework import serializers
from .models import Category,SubCategory
from django.db import transaction

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('subcategories')
        with transaction.atomic():
            category = Category.objects.create(**validated_data)
            sub_category = [SubCategory(category=category, **item_data) for item_data in items_data]
            SubCategory.objects.bulk_create(sub_category)
        return category


