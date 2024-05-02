from django.shortcuts import render
from rest_framework.generics import GenericAPIView , ListAPIView
from product.models import Product
from compare.serializers import CampareSerializer ,CampareItemSerializer

from .models import Compare , CompareIteam
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class AddToCompareView(GenericAPIView):
    serializer_class = CampareItemSerializer
    def post(self,request,input):
        id = input
        products = []
        compare_id = None
        compare_data = None
        products = request.data.get('product_ids')
        
        if Compare.objects.get(user_id=id) is None:
         user_id = {'user_id': input}
         print(user_id)
         serializer = CampareSerializer(data=user_id)
         serializer.is_valid(raise_exception=True)
         compare_data = serializer.save()
        else:
           compare_data =Compare.objects.get(user_id = id)
        
        data= {
            "compare_id" : compare_data.compare_id,
            "product_ids" :products
        }
        comapre_items = CampareItemSerializer(data=data)
        comapre_items.is_valid(raise_exception=True)
        comapre_items.save()

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Product added to compare successfully',
            'compare_id' : compare_data.compare_id
            
        },status=200)
class CompareView(ListAPIView):
       serializer_class = CampareItemSerializer
       def get (self,request,input):
           id = input
           items  = CompareIteam.objects.filter(compare_id=id)
           serializer = CampareItemSerializer(items ,many= True)
           
           return Response({
            'status': status.HTTP_200_OK,
            'message': 'data retrived successfully',
            'data' :serializer.data
            
            },status=200)



