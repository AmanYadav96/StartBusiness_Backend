from django.urls import path
from .views import *


urlpatterns = [
    path('add',OrderAddView.as_view(), name = 'Order add'),
    path('view/',OrderView.as_view(), name = 'Order views'),
    path('view/<uuid:input>/',OrderView.as_view(), name = 'Order views single'),
    # path('update/<uuid:input>/',OrderItemUpdateView.as_view(), name = 'Order update '),
    # path('deleteItem/<uuid:input>',OrderDeleteView.as_view(), name = 'Order delete'),
    # path('addItem',OrderItemAddView.as_view(), name = 'Order_item add'),

]