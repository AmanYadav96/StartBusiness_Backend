from rest_framework.generics import GenericAPIView,ListAPIView
from StartBusiness.filter import BrandFilter
from brand.models import Brand
from brand.serializers import BrandSerializer,DealerViewAccordingBrandSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from StartBusiness.s3_image_config import delete_file, upload_base64_file
from StartBusiness.custom_paginations import CustomPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from dealer.models import Dealer
from rest_framework.parsers import BaseParser , JSONParser
import json
from dealer.serializers import DealerSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from user.customepermission import IsAdmin


# add brand
class ListParser(BaseParser):
    def parse(self, stream, media_type=None, parser_context=None):
        data = json.load(stream)
        return data

# parser_classes = [ListParser]
class BrandAddView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = BrandSerializer
    def post(self , request):
            serializer = BrandSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
            "status" :status.HTTP_201_CREATED,
            "message":"Brand is added successfully",
            }, status=201
            )


# get all brands and get one brand by id
class BrandAllView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Brand.objects.all().order_by('-created_at')
    filter_backends = [OrderingFilter, SearchFilter,DjangoFilterBackend]
    pagination_class = CustomPagination
    serializer_class = BrandSerializer
    ordering_fields = ['created_at']
    search_fields = ['category','dealer','is_active']
    filterset_class = BrandFilter
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data == []:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                "message":"No Data Found!!"
            },status=404)
        return Response({
            'status':status.HTTP_200_OK,
            "message":'brand data retrieved successfully ',
            'data':response.data
        },status=200)

class BrandView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, input=None, format=None):
            _id = input
            try:
                brand  = Brand.objects.get(brand_id=_id)
                serializer = BrandSerializer(brand)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': "brand " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Brand.DoesNotExist:
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                        'message': "brand not found",
                    },
                    status=404
                )
  
    
# update brand
class UpdateBrandView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = BrandSerializer
    def patch(self, request, input, format=None):
       _id = input
       try:
        brand = Brand.objects.get(brand_id=_id)
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
             'status':status.HTTP_200_OK,
             'message': "brand updated successfully"
        },status=200)
       except Brand.DoesNotExist:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'brand id not found'
        },status=404)
     
       
# delete brand
class DeleteBrandView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def delete(self, request, input, format=None):
        _id = input
        try:
            print(_id)
            brand = Brand.objects.get(brand_id=_id)
            # file = brand.brand_logo
            # file = file.name
            # delete_file(file)
            brand.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Brand Deleted Successfully' 
            },
            status=200)
        except Brand.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid Brand_id',
            },
            status=404)
    


class DealerViewAccordingBrand(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = DealerViewAccordingBrandSerializer
    # parser_classes = [ListParser]
    def post(self, request, format=None):
        serializer =DealerViewAccordingBrandSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        dealers_id = serializer.data.get('dealer')
        dataa = []
        for id in dealers_id:
            data = Dealer.objects.get(dealer_id=id)
            dataa.append(data)
        dealers = DealerSerializer(dataa,many=True)
        return Response({
            'status':status.HTTP_200_OK,
            "message":"data retrives successfully",
            'data':dealers.data
        },status=200)