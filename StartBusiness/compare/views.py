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
        serializer = CampareItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Product added to compare successfully',
            'compare_id' : serializer.data
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



