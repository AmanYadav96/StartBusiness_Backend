from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from order.models import Order
from order.serializers import OrderSerializer

# add Order
class OrderAddView(GenericAPIView):
    serializer_class = OrderSerializer
    def post(self, request , format=None):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "message":"Order Added Successfully",
            'order': order.order_id
        })
  
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
        


class OrderViewByUserId(APIView):
    serializer_class = OrderSerializer
    def get(self, request, user_id):
       try:
            _id = user_id
            order = Order.objects.filter(user=_id)
            serializer = OrderSerializer(order, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'order retrieved Successfully',
                'data':serializer.data
            },status=200)
       except Order.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid user_id'
            }, status=status.HTTP_404_NOT_FOUND)
