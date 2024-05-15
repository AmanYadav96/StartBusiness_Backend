from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from order.models import Order,OrderItem
from order.serializers import OrderSerializer,OrderItemSerializer

# add Order
class OrderAddView(GenericAPIView):
    serializer_class = OrderSerializer
    def post(self, request,format=None):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        print(serializer)


        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Order added successfully',
            'order_id':order.order_id,
        },status=201)


# update Order
class OrderItemUpdateView(GenericAPIView):
    serializer_class = OrderItemSerializer
    def patch(self, request, input):
        _id = input
        try:
           order_item = OrderItem.objects.get(order_item_id=_id)
           serializer = OrderSerializer(order_item, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Order item Updated Successfully'  
                },status=200)
        except Order.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid Order_item_id',
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
            order_item = OrderItem.objects.get(order_item_id=_id)
            order_item.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Order item Deleted Successfully'
            },status=200)
        except Order.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid Order_item_id'
            }, status=status.HTTP_404_NOT_FOUND)

# order item add
class OrderItemAddView(GenericAPIView):
    serializer_class = OrderItemSerializer
    def post(self, request,format=None):
        serializer = OrderItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Order item added successfully',
            'data':serializer.data
        },status=201)

