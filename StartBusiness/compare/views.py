from django.shortcuts import render
from rest_framework.generics import GenericAPIView , ListAPIView
from product.models import Product
from compare.serializers import CampareSerializer ,CampareItemSerializer
from rest_framework.views import APIView
from .models import Compare , CompareItem
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user.customepermission import IsCustomer
# Create your views here.

class AddToCompareView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsCustomer]
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
       permission_classes = [IsAuthenticated,IsCustomer]
       serializer_class = CampareItemSerializer
       def get (self,request,compare_id):
           try:
               _id = compare_id
               items  = CompareItem.objects.filter(compare_id=_id).order_by('-created_at')
               serializer = CampareItemSerializer(items ,many= True)
               return Response({
                'status': status.HTTP_200_OK,
                'message': 'data retrived successfully',
                'data' :serializer.data
                },status=200)
           except CompareItem.DoesNotExist:
               return Response({
                    'status': status.HTTP_404_NOT_FOUND,
                    'message': 'compare item not found'
                    },status=404)
           


class CompareDeleteView(APIView):
    permission_classes = [IsAuthenticated,IsCustomer]
    def delete(self, request, compare_item_id):
        _id = compare_item_id
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

class CompareDeleteAllView(APIView):
    permission_classes = [IsAuthenticated,IsCustomer]
    def delete(self, request,compare_id):
        _id = compare_id
        try:
            compare = CompareItem.objects.filter(compare_id=_id)
            for i in compare:
                i.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Compare All Item Deleted Successfully' 
            },
            status=200)
        except CompareItem.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid Compare_id',
            },
            status=404)