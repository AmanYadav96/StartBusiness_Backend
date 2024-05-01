from rest_framework import serializers

from .models import CompareIteam,Compare


class CampareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compare
        fields = ["compare_id","user_id"]

    


class CampareItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompareIteam
        fields = "__all__"

    