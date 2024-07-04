from order.filter import OrderFilter
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.customepermission import IsAdmin, IsCustomer
from StartBusiness.custom_paginations import CustomPagination
from .serializers import OrderSerializer
from .tasks import calculate_total_price

# add Order
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

# order update by order_id
class OrderUpdateView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = OrderSerializer
    def patch(self, request, order_id, format=None):
      _id = order_id
      try:
            print(_id)
            order = Order.objects.get(order_id=_id)
            serializer = OrderSerializer(order, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
             'status': status.HTTP_200_OK,
             'message': "order updated successfully"
        },status=200)
      except Order.DoesNotExist:
            return Response({
                 'status': status.HTTP_404_NOT_FOUND,
                'message':'order id not found'
        },status=404)

# get all order
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
        

# get all order by particular user
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


# get order by order_id
class OrderView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = OrderSerializer
    def get(self, request, order_id, format=None):
        _id = order_id
        try:
            order = Order.objects.get(order_id=_id)
            serializer = OrderSerializer(order)
            return Response({
                'status': status.HTTP_200_OK,
                'message': "order retrieved successfully",
                'data': serializer.data
                },status=200)
        except Order.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'order id not found'
                },status=404)

           