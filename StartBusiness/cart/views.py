from cart.filter import CartFilter
from cart.models import Cart
from cart.serializers import CartSerializer,CartViewSerializer,CartUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView , ListAPIView
from rest_framework.views import APIView


class CartRegisterView(GenericAPIView):
    serializer_class = CartSerializer
    def post(self, request,format=None):
        serializer = CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Cart Registered',
        },status=201)

class CartView(ListAPIView):
   queryset = Cart.objects.all()
   serializer_class = CartViewSerializer
   filterset_class = CartFilter
   
   def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data == []:
            return Response({
                "message":"No Data Found!!"
            })
        return Response(
               {
                  'status': status.HTTP_200_OK,
                  'message': 'Cart data retrieved successfully',
                  'data': response.data
               },status=200
            )
class CartViewById(APIView):
    
    def get(self,request, input = None,format=None):
        _id = input
        try:
            cart = Cart.objects.get(cart_id=_id)
            serializer = CartViewSerializer(cart)
            return Response({
                'status':status.HTTP_200_OK,
                'message': "Cart data retrived",
                'data':serializer.data
            },status=200)
        except Cart.DoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message': "Invalid Cart id"
            },
            status=400)
       
        
class CartUpdateView(GenericAPIView):
    serializer_class = CartUpdateSerializer
    def patch(self, request, input, format=None):
        _id = input
        try:
           cart = Cart.objects.get(cart_id=_id)
           serializer = CartUpdateSerializer(cart, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Cart Updated Successfully'  
                },status=200)
        except Cart.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid id',
                },
                status=400)
        

class CartDeleteView(APIView):
    def delete(self, request, input):
        _id = input
        try:
            cart = Cart.objects.get(cart_id=_id)
            cart.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Cart Deleted Successfully' 
            },
            status=200)
        except Cart.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid Cart_id',
            },
            status=400)


import requests
import json
import uuid
import random


# Convert UUID to a string for use in JSON
amount = 456

class paymentView(APIView):


# Variables from the previous PHP script
 

# Setting up the payload
 def post(self, request,format=None):
    cust_mobileno = '9691279019'  # Normally would be a real phone number
    cust_email_id = 'virajgurjar789@gmail.com'
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
    'link_amount': amount,
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
   
# class CartRegisterView(APIView):
 
#     def post(self, request,format=None):
         
#         return Response({
#             'status':status.HTTP_201_CREATED,
#             "msg":'Cart Registered',
#         },status=201)