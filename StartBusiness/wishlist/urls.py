from django.urls import path
from .views import *


urlpatterns = [
    path('add/',WishlistAddView.as_view(), name = 'AddToWishlist'),
    path('delete/<uuid:wishlist_item_id>/',WishlistDeleteView.as_view(),name=' delete wishlist item'),
    path('view/<uuid:wishlist_id>/',WishlistViewById.as_view(), name = 'AddToWishlist')
    

]