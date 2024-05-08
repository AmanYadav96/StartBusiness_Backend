from rest_framework import serializers

from .models import CompareItem,Compare


class CampareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compare
        fields = ["compare_id","user_id"]

    


class CampareItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompareItem
        fields = "__all__"

    