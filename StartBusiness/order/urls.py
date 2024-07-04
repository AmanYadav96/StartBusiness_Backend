from django.urls import path
from .views import *


urlpatterns = [
    path('add',OrderAddView.as_view(), name = 'Order add'),
    path('view/',OrderAllView.as_view(), name = 'Order views'),
    path('viewsByUserId/',OrderViewByUserId.as_view(),name='Order views bu userid'),
    path('update/<uuid:order_id>',OrderUpdateView.as_view(),name='order update by order_id'),
    path('view/<uuid:order_id>',OrderView.as_view(),name='order view by order_id'),

    
    

]