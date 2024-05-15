from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from payment.models import Payment
from rest_framework.generics import GenericAPIView
from payment.serializers import PaymentSerializer
# Create your views here.

import requests
import json
import uuid
import random


class PaymentAddView(GenericAPIView):
   serializer_class = PaymentSerializer
   def post(self, request,format=None):
    serializer = PaymentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    cust_mobileno = request.data['user_mobile_no']  # Normally would be a real phone number
    cust_email_id = request.data['user_email']
    random_number = str(random.randint(1000, 9999))  
    payload = {
    'customer_details': {
        'customer_phone': cust_mobileno,
        'customer_email': cust_email_id
    },
    'link_notify': {
        'send_sms': True,
        'send_email': True
    },
    'link_id': random_number,
    'link_amount': request.data['amount'],
    'link_currency': 'INR',
    'link_purpose': 'Payment for PlayStation 11'
    }
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-version": "2022-09-01",
    "x-client-id": "TEST10179942e8043908e93703776ae424997101",  # Replace with your actual client ID
    "x-client-secret": "cfsk_ma_test_10e52740b1c67115a7ba465151154371_0c1df231"  # Replace with your actual secret key
    }


# Making the POST request
    response = requests.post("https://sandbox.cashfree.com/pg/links", 
                         data=json.dumps(payload), headers=headers, timeout=30)

# Handling the response
    if response.status_code == 200:
     result = response.json()
     serializer.save()
    # Assuming result['link_url'] exists
     redirect_url = result['link_url']
     print("Redirect to:", redirect_url)
    else:
       print("Failed to create payment link:", response.status_code, response.text)
    return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Cart Registered',
            'link': redirect_url
        },status=201)
        
         


class PaymentView(APIView):
    serializer_class = PaymentSerializer
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                payment  = Payment.objects.get(payment_id=_id)
                serializer = PaymentSerializer(payment)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Payment data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Payment.DoesNotExist:
                return Response(
                    {
                        'status':  status.HTTP_404_NOT_FOUND,
                        'message': "invalid payment_id",
                    },
                    status=404
                )
        else:
            payment = Payment.objects.all()
            serializer = PaymentSerializer(payment, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Payment data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

class PaymentUpdateView(GenericAPIView):
    serializer_class = PaymentSerializer
    def patch(self, request, input):
        _id = input
        try:
           payment = Payment.objects.get(payment_id=_id)
           serializer = PaymentSerializer(payment, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Payment Updated Successfully',
                'data': serializer.data
                },status=200)
        except payment.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid payment_id',
                },
                status=404)

class PaymentDeleteView(APIView):
    def delete(self, request, input):
        try:
            _id = input
            order = Payment.objects.get(payment_id=_id)
            order.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Payment Deleted Successfully'
            },status=200)
        except Payment.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid Payment_id'
            }, status=status.HTTP_404_NOT_FOUND)



    
   
class callback(APIView):
 
    def post(self, request,format=None):
        print(request.data)
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Cart Registered',
        },status=201)