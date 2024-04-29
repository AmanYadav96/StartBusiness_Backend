from django.urls import path
from .views import *


urlpatterns = [
    path('add',CartRegisterView.as_view(), name = 'Cart register'),
    path('view/',CartView.as_view(), name = 'Cart views'),
    path('view/<uuid:input>/',CartViewById.as_view(), name = 'Cart views single'),
    path('update/<uuid:input>/',CartUpdateView.as_view(), name = 'Cart update '),
    path('delete/<uuid:input>',CartDeleteView.as_view(), name = 'Cart delete'),
    path('payment',paymentView.as_view(), name = 'Cart register'),
    path('callback',paymentView.as_view(), name = 'Cart register'),

]