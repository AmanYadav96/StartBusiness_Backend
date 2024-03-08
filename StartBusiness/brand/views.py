from rest_framework.generics import GenericAPIView,ListAPIView
from StartBusiness.filter import BrandFilter
from brand.models import Brand
from brand.serializers import BrandSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from StartBusiness.s3_image_config import upload_base64_file
from StartBusiness.custom_paginations import CustomPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# add brand
class BrandAddView(GenericAPIView):
    serializer_class = BrandSerializer
    def post(self , request):
            serializer = BrandSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            file = request.data.get('brand_logo')
            data=upload_base64_file(file,'brand')
            serializer.validated_data['brand_logo']= data
            serializer.save()

            return Response({
            "status" :"success",
            "message":"Brand is added successfully",
            }, status=status.HTTP_201_CREATED
            )


# get all brands and get one brand by id
class BrandAllView(ListAPIView):
    queryset = Brand.objects.all().order_by('created_at')
    filter_backends = [OrderingFilter, SearchFilter,DjangoFilterBackend]
    pagination_class = CustomPagination
    serializer_class = BrandSerializer
    ordering_fields = ['created_at']
    search_fields = ['category','dealer','is_active']
    filterset_class = BrandFilter
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        
        
        return Response({
            'status':status.HTTP_200_OK,
            "message":'brand data retrieved successfully ',
            'data':response.data
        },status=200)

class BrandView(APIView):
    def get(self, request, input=None, format=None):
            _id = input
      
            if Brand.objects.filter(brand_id=_id).count() > 0:
                brand  = Brand.objects.get(brand_id=_id)
                serializer = BrandSerializer(brand)


                return Response(
                    {
                        'status': 'success',
                        'message': "brand " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=status.HTTP_200_OK
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "brand not found",
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
  
    
# update brand
class UpdateBrandView(APIView):
    def patch(self, request, input, format=None):
       _id = input
       if _id is not None:
        brand = Brand.objects.get(brand_id=_id)
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if request.data.get('brand_logo') is not None:
           file = request.data.get('brand_logo')
           data=upload_base64_file(file,'brand')
           serializer.validated_data['brand_logo']= data
        
        
        serializer.save()
        return Response({
             'status': 'success',
             'message': "brand updated successfully"
        },status=status.HTTP_200_OK)
       else:
            return Response({
                'status':'brand id not found'
        },status=status.HTTP_404_NOT_FOUND)
     
       
# delete brand
class DeleteBrandView(APIView):
    def delete(self, request, input, format=None):
        _id = input
        brand = Brand.objects.get(brand_id=_id)
        if _id is not None:
            brand.delete()
            return Response({
            'status': 'success',
            'message': "brand deleted successfully"
        }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'failure',
                'message': "No such brand id exists for delete."
                }, status=status.HTTP_404_NOT_FOUND)
    


