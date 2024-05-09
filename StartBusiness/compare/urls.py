from django.urls import path
from .views import *


urlpatterns = [
    path('add/',AddToCompareView.as_view(), name = 'AddToCompare'),
    path('delete/<uuid:compare_item_id>/',CompareDeleteView.as_view(),name=' delete compare item'),
    path('deleteAll/<uuid:compare_id>/',CompareDeleteAllView.as_view(),name='delete all comapre them'),
    path('view/<uuid:input>/',CompareView.as_view(), name = 'AddToCompare')
    

]