from django.urls import path
from .views import *


urlpatterns = [
    path('add',OrderAddView.as_view(), name = 'Order add'),
    path('view/',OrderAllView.as_view(), name = 'Order views'),
    path('viewsByUserId/',OrderViewByUserId.as_view(),name='Order views bu userid')
    
    

]