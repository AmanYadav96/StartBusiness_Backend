from django.urls import path
from .views import *


urlpatterns = [
    path('add/',CartAddView.as_view(), name = 'Cart register'),
    path('view/',CartView.as_view(), name = 'Cart views'),
    path('view',CartViewById.as_view(), name = 'Cart views single'),
    path('update/<uuid:input>/',CartUpdateView.as_view(), name = 'Cart update '),
    path('delete/<uuid:input>',CartDeleteView.as_view(), name = 'Cart delete'),
    path('deleteAll/<uuid:cart_id>',CartDeleteAllView.as_view(), name = 'Cart delete'),

]