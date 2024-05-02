from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from order.models import Order
from order.serializers import OrderSerializer

# add Order
class OrderAddView(GenericAPIView):
    serializer_class = OrderSerializer
    def post(self, request,format=None):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Order added successfully'
        },status=201)


# update Order
class OrderUpdateView(GenericAPIView):
    serializer_class = OrderSerializer
    def patch(self, request, input):
        _id = input
        try:
           order = Order.objects.get(order_id=_id)
           serializer = OrderSerializer(order, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Order Updated Successfully'  
                },status=200)
        except Order.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid Order_id',
                },
                status=404)

# get Order or get Order by id   
class OrderView(APIView):
    serializer_class = OrderSerializer
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                order  = Order.objects.get(order_id=_id)
                serializer = OrderSerializer(order)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Order data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Order.DoesNotExist:
                return Response(
                    {
                        'status':  status.HTTP_404_NOT_FOUND,
                        'message': "Order data not found",
                    },
                    status=404
                )
        else:
            order = Order.objects.all()
            serializer = OrderSerializer(order, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Order data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

# delete Order
class OrderDeleteView(APIView):
    def delete(self, request, input):
        try:
            _id = input
            order = Order.objects.get(Order_id=_id)
            order.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Order Deleted Successfully'
            },status=200)
        except Order.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid Order_id'
            }, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
