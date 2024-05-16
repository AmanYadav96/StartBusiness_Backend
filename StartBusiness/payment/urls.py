from django.urls import path
from .views import *


urlpatterns = [
    path('add/',PaymentAddView.as_view(), name = 'Payment add'),
    path('view/',PaymentView.as_view(), name = 'Payment views'),
    path('view/<uuid:input>/',PaymentView.as_view(), name = 'Payment views single'),
    path('update/<uuid:input>/',PaymentUpdateView.as_view(), name = 'Payment update '),
    path('delete/<uuid:input>/',PaymentDeleteView.as_view(), name = 'payment delete'),
    path('callback/',callback.as_view(), name = 'Payment add'),
]