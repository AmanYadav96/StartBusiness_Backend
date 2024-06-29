from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView
from StartBusiness.custom_paginations import CustomPagination
from order.filter import OrderFilter
from product.models import Product
from cart.models import CartItem
from order.models import OrderItem,Order
from order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from user.customepermission import IsCustomer,DenyForAllUser,IsAdmin

# add Order

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import OrderIdSerializer, OrderSerializer
from .tasks import calculate_total_price
class OrderAddView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsCustomer]
    serializer_class = OrderSerializer
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        items = serializer.validated_data.get('items', [])
        order = serializer.save(total_price=calculate_total_price(items))
        return Response({
            'status': status.HTTP_201_CREATED,
            'message': "Order Added Successfully",
            'order': order.order_id
        })

class OrderAllView(ListAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    queryset = Order.objects.all().order_by('-created_at')
    pagination_class = CustomPagination
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data == []:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                "message":"No Data Found!!"
            },status=404)
        return Response({
            'status':status.HTTP_200_OK,
            "message":'Order data retrieved successfully ',
            'data':response.data
        },status=200)
        


class OrderViewByUserId(ListAPIView):
    permission_classes = [IsAuthenticated,IsCustomer]
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data == []:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'Data not found!!'
            },status=404)
        return Response({
            'status':status.HTTP_200_OK,
            'message':'Order data retrieved successfully ',
            'data':response.data
        },status=200)

