from django.urls import path
from .views import *


urlpatterns = [
    path('add/<uuid:input>/',AddToCompareView.as_view(), name = 'AddToCompare'),
    path('view/<uuid:input>/',CompareView.as_view(), name = 'AddToCompare')
    

]