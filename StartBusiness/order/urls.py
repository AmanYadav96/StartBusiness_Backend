from django.urls import path
from .views import *


urlpatterns = [
    path('add',OrderAddView.as_view(), name = 'Order add'),
    path('view/',OrderView.as_view(), name = 'Order views'),
    path('view/<uuid:input>/',OrderView.as_view(), name = 'Order views single'),
    path('update/<uuid:input>/',OrderUpdateView.as_view(), name = 'Order update '),
    path('delete/<uuid:input>',OrderDeleteView.as_view(), name = 'Order delete'),

]