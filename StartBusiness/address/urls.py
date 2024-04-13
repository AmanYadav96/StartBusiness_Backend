from django.urls import path
from .views import *


urlpatterns = [
    path('add',AddressAddView.as_view(), name = 'Address add'),
    path('view/',AddressView.as_view(), name = 'Address views'),
    path('view/<uuid:input>/',AddressView.as_view(), name = 'Address views single'),
    path('update/<uuid:input>/',AddressUpdateView.as_view(), name = 'Address update '),
    path('delete/<uuid:input>',AddressDeleteView.as_view(), name = 'Address delete'),

]