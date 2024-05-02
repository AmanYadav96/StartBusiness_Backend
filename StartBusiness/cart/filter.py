from django_filters import FilterSet
from cart.models import Cart

class CartFilter(FilterSet):
    class Meta:
        model = Cart
        fields = ['user']