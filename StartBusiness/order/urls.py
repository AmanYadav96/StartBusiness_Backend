from django.urls import path
from .views import *


urlpatterns = [
    path('add',OrderAddView.as_view(), name = 'Order add'),
    path('view/',OrderView.as_view(), name = 'Order views'),
    path('view/<uuid:user_id>/',OrderViewByUserId.as_view(),name='Order views bu userid'),
    path('view/<uuid:input>/',OrderView.as_view(), name = 'Order views single')

]