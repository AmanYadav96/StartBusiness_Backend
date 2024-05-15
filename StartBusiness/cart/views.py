from cart.filter import CartFilter
from .serializers import CartItemSerializer, CartViewSerializer
from user.models import User
from product.models import Product
from cart.models import Cart
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView , ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartItem


class CartAddView(GenericAPIView):
    serializer_class = CartItemSerializer 
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
                'status':status.HTTP_201_CREATED,
                'message':'Cart item created successfully',
                'data':serializer.data
            },status=201)


class CartView(ListAPIView):
   queryset = CartItem.objects.all()
   serializer_class = CartViewSerializer
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
    queryset = CartItem.objects.all()
    serializer_class = CartViewSerializer

    def get(self, request, format=None):
        _id = request.query_params.get('user_id')
        try:
            cart = Cart.objects.get(user=_id)
            cart_items = CartItem.objects.filter(cart=cart)
            serializer = CartViewSerializer(cart_items, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'message': "Cart data retrieved",
                'data': serializer.data
            })
        except Cart.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': "Invalid Cart id"
            }, status=400)

        
class CartUpdateView(GenericAPIView):
    serializer_class = CartItemSerializer
    def patch(self, request, input, format=None):
        _id = input
        try:
           cart = CartItem.objects.get(cart_item_id=_id)
           serializer = CartItemSerializer(cart, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Cart Item Updated Successfully'  
                },status=200)
        except CartItem.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid id',
                },
                status=400)
        

class CartDeleteView(APIView):
    def delete(self, request, input):
        _id = input
        try:
            cart = CartItem.objects.get(cart_item_id=_id)
            cart.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Cart Item Deleted Successfully' 
            },
            status=200)
        except CartItem.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid Cart_id',
            },
            status=400)





# Convert UUID to a string for use in JSON


