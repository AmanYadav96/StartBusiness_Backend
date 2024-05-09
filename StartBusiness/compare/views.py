from django.shortcuts import render
from rest_framework.generics import GenericAPIView , ListAPIView
from product.models import Product
from compare.serializers import CampareSerializer ,CampareItemSerializer
from rest_framework.views import APIView
from .models import Compare , CompareItem
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class AddToCompareView(GenericAPIView):
    serializer_class = CampareItemSerializer
    def post(self,request,format=None):
        
        
        comapre_items = CampareItemSerializer(data=request.data)
        comapre_items.is_valid(raise_exception=True)
        comapre_items.save()

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Product added to compare successfully',
           
        },status=200)

class CompareView(APIView):
       serializer_class = CampareItemSerializer
       def get (self,request,input):
           id = input
           items  = CompareItem.objects.filter(compare_id=id)
           serializer = CampareItemSerializer(items ,many= True)
           
           return Response({
            'status': status.HTTP_200_OK,
            'message': 'data retrived successfully',
            'data' :serializer.data
            
            },status=200)


class CompareDeleteView(APIView):
    def delete(self, request, input):
        _id = input
        try:
            compare = CompareItem.objects.get(compare_item_id=_id)
            compare.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Compare Item Deleted Successfully' 
            },
            status=200)
        except CompareItem.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid Compare_item_id',
            },
            status=404)
