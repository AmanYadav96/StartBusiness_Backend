from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView
from invoice.filter import InvoiceFilter
from invoice.models import Invoice
from rest_framework.views import APIView
from invoice.serializers import InvoiceSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from user.customepermission import IsAdmin
from rest_framework.response import Response
from rest_framework import status
from StartBusiness.custom_paginations import CustomPagination
# Create your views here.
class InvoiceAddView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = InvoiceSerializer
    def post(self, request,format=None):
        serializer = InvoiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invoice = serializer.save()
        print(invoice)
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Invoice added successfully',
            'invoice':invoice.invoice_id
        },status=201)

class UpdateInvoiceView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = InvoiceSerializer
    def patch(self, request, input, format=None):
       _id = input
       try:
        invoice = Invoice.objects.get(invoice_id=_id)
        serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
             'status':status.HTTP_200_OK,
             'message': "Invoice updated successfully"
        },status=200)
       except Invoice.DoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'Invoice id not found'
        },status=404)
       
class DeleteInvoiceView(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, input, format=None):
        _id = input
        try:
            print(_id)
            invoice = Invoice.objects.get(invoice_id=_id)
            invoice.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Invoice Deleted Successfully' 
            },
            status=200)
        except Invoice.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid Invoice_id',
            },
            status=404)
        
class InvoiceAllView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Invoice.objects.all().order_by('-created_at')
    pagination_class = CustomPagination
    serializer_class = InvoiceSerializer
    filterset_class = InvoiceFilter
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data == []:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                "message":"No Data Found!!"
            },status=404)
        return Response({
            'status':status.HTTP_200_OK,
            "message":'Invoice data retrieved successfully ',
            'data':response.data
        },status=200)

class InvoiceView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, input=None, format=None):
            _id = input
            try:
                invoice  = Invoice.objects.get(invoice_id=_id)
                serializer = InvoiceSerializer(invoice)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': "Invoice " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Invoice.DoesNotExist:
                return Response(
                    {
                        'status':  status.HTTP_404_NOT_FOUND,
                        'message': "Invoice not found",
                    },
                    status=404
                ) 