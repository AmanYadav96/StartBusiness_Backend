from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView
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

class OrderView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]  #check
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
            order = Order.objects.all().order_by('-created_at')
            serializer = OrderSerializer(order, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Order data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        


class OrderViewByUserId(ListAPIView):
    permission_classes = [AllowAny]
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
    

class OrderIdView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = OrderIdSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_ids = serializer.validated_data.get('order_id')
        print(order_ids)

        response_data = []
        for _id in order_ids:
            try:
                order_items = OrderItem.objects.filter(order__order_id=_id)
                if not order_items.exists():
                    raise OrderItem.DoesNotExist
                for order_item in order_items:
                    response_data.append({
                        "order_id": order_item.order.order_id,
                        "order_date": order_item.order.created_at,
                        "product_image": order_item.product.image.url,
                        "product_name": order_item.product.name,
                        "product_category": order_item.product.category.category_name,
                        "customer_name": order_item.order.user.user_name,
                        "price": order_item.order.total_price,
                    })
            except OrderItem.DoesNotExist:
                response_data.append({
                    'order_id': _id,
                    'error': f"No product found with this order id: {_id}",
                })

        return Response({
            'order': response_data,
        }, status=status.HTTP_200_OK)
