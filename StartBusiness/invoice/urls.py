from django.urls import path, include
from invoice.views import InvoiceAddView,UpdateInvoiceView,DeleteInvoiceView,InvoiceView

urlpatterns = [
    path('add/',InvoiceAddView.as_view(),name="Invoice add"),
    path('update/<uuid:input>/',UpdateInvoiceView.as_view(),name="update manager by id"),
    path('delete/<uuid:input>/',DeleteInvoiceView.as_view() ,name='delete manager by id'),
    path('view/<uuid:input>/',InvoiceView.as_view(),name='Invoice view by id'),
    path('view/',InvoiceView.as_view(),name='Invoice view')
]