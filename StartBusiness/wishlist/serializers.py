from rest_framework import serializers
from .models import Wishlist,WishlistItems



class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItems
        fields = "__all__"

    