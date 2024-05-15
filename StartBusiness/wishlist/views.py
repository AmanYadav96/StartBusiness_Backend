
from .serializers import WishlistItemSerializer
from user.models import User
from product.models import Product
from wishlist.models import Wishlist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView , ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wishlist,WishlistItems

class WishlistAddView(GenericAPIView):
    serializer_class = WishlistItemSerializer 
    def post(self, request):
        serializer = WishlistItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
                'status':status.HTTP_201_CREATED,
                'message':'Wishlist item created successfully',
                'data':serializer.data
            },status=201)


class WishlistViewById(APIView):
       serializer_class = WishlistItemSerializer
       def get (self,request,wishlist_id):
           _id = wishlist_id
           items  = WishlistItems.objects.filter(wishlist_id=_id)
           serializer = WishlistItemSerializer(items ,many= True)
           
           return Response({
            'status': status.HTTP_200_OK,
            'message': 'data retrived successfully',
            'data' :serializer.data
            
            },status=200)

        

class WishlistDeleteView(APIView):
    def delete(self, request, wishlist_item_id):
        _id = wishlist_item_id
        try:
            wishlist = WishlistItems.objects.get(wishlist_items_id=_id)
            wishlist.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Wishlist Item Deleted Successfully' 
            },
            status=200)
        except WishlistItems.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid Wishlist_id',
            },
            status=400)
