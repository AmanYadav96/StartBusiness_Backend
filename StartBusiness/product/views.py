import uuid
from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from product.filter import ProductFilter
from StartBusiness.s3_image_config import delete_file
from product.serializers import *
from .models import Product
from rest_framework.views import APIView
from rest_framework import status
from StartBusiness.custom_paginations import CustomPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from category.models import Category
from user.customepermission import IsAdmin
from rest_framework.permissions import IsAuthenticated ,AllowAny
from brand.models import Brand
# register 01
class ProductRegisterView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductSerializer
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['counter'] = 1
        serializer.save()
       
        return Response({
            'status' :status.HTTP_201_CREATED,
            'message':'Product is added successfully',
            'product_id':serializer.data['product_id'],
            # 'product_id':serializer
            }, status=201
  
        ) 


# View Product Full
class ProductAllView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductFullDetailsSerializer
    pagination_class = CustomPagination
    filterset_class = ProductFilter
    ordering_fields = ['created_at']
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data == []:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':'Data not found!!'
            },status=404)
        return Response({
            'status':status.HTTP_200_OK,
            'message':'product data retrieved successfully ',
            'data':response.data
        },status=200)

    

class ProductView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        try:
            product  = Product.objects.get(product_id=_id)
            serializer = ProductFullDetailsSerializer(product)
            return Response(
                {
                    'status': 'success',
                    'message': 'Product data retrieved successfully',
                    'data': serializer.data,
                }, status=200
            )
        except Product.DoesNotExist:
            return Response(
                    {
                        'status':  status.HTTP_404_NOT_FOUND,
                        'message': 'Product not found',
                    },
                    status=404
        )
    
    

class UpdateProductView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductSerializer
    def patch(self, request, input, format=None):
        _id = input
        try:
            product = Product.objects.get(product_id=_id)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
             'status': status.HTTP_200_OK,
             'message': 'Product updated successfully'
        },status=200)
        except Product.DoesNotExist:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
        },status=404)
    

class DeleteProductView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def delete(self, request, input, format=None):
        _id = input
        try:
            product = Product.objects.get(product_id=_id)
            product.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Product Deleted Successfully' 
            },
            status=200)
        except Product.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid product id',
            },
            status=404)
   
        

# Other ----------------------------------------------------------
        
 # Product update media
class ProductMediaView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductMediaSerializer
    def patch(self,request ,input):
        _id = input
        try:
            product = Product.objects.get(product_id=_id)
            serializer = ProductMediaSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 2
            serializer.save()
            return Response({
             'status':status.HTTP_200_OK,
             'message': 'Product updated successfully'
        },status=200)
        except Product.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'status':'Product id not found'
        },status=404)

# Product Details View
class ProductDetailsView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductDetailsSerializer
    def patch(self,request ,input):
        _id = input
        try:
            product = Product.objects.get(product_id=_id)
            serializer = ProductDetailsSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 3
            serializer.save()
            return Response({
             'status': status.HTTP_200_OK,
             'message': 'Product updated successfully'
        },status=200)
        except Product.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
        },status=404)



   # Pricing update
class PricingView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductPricingSerializer
    def patch(self,request ,input):
        _id = input
        try:
            product = Product.objects.get(product_id=_id)
            serializer = ProductPricingSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 4
            serializer.save()
            return Response({
             'status': status.HTTP_200_OK,
             'message': 'Product updated successfully'
        },status=200)
        except Product.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
        },status=404)
    # Product update inventory
class InventoryView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductInventorySerializer
    def patch(self,request ,input):
        _id = input
        try:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductInventorySerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 5
            serializer.save()
            return Response({
             'status': status.HTTP_200_OK,
             'message': 'Product updated successfully'
        },status=200)
        except Product.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
        },status=404)
    

    # Product Variants View
class ProductVariantsView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductVariantsSerializer
    def patch(self,request ,input):
        _id = input
        try:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductVariantsSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 6
            serializer.save()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Product updated successfully'
        },status=200)
        except Product.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
        },status=404)

# Product additional information update
    
class ProductAdditionalView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = AdditionalInfoSerializer
    def patch(self,request ,input):
        _id = input
        try:
            product = Product.objects.get(product_id=_id)
            serializer = AdditionalInfoSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 7
            serializer.save()
            return Response({
             'status': status.HTTP_200_OK,
             'message': 'Product updated successfully'
        },status=200)
        except Product.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
        },status=404)

# Seo info update 
class SeoInformationView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductSeoSerializer
    def patch(self,request ,input):
        _id = input
        try:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductSeoSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 8
            serializer.save()
            return Response({
             'status': status.HTTP_200_OK,
             'message': 'Product updated successfully'
        },status=200)
        except Product.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
        },status=404)
       
    
    
# ---------------------------------------------------------------------
class BasicProductAllView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductSerializer(product)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Product data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductSerializer(product, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Product data retrieved successfully',
                 'data': serializer.data,
            }, status=200)


# media all view
class ProductMediaAllView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductMediaSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductMediaSerializer(product)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Product data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Product.DoesNotExist:
                return Response(
                    {'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductMediaSerializer(product, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Product data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

# product details all view
class OtherDetailsAllView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductDetailsSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductDetailsSerializer(product)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Product data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
                    },status=404)
        else:
            product = Product.objects.all()    
            serializer = ProductDetailsSerializer(product, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Product data retrieved successfully',
                 'data': serializer.data,
            }, status=200)

# pricing all view
class PricingAllView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductPricingSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductPricingSerializer(product)
                return Response(
                    {
                        'status':status.HTTP_200_OK,
                        'message': 'Product data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductPricingSerializer(product, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Product data retrieved successfully',
                 'data': serializer.data,
            }, status=200)

# product tax view all

class ProductInventoryAllView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductInventorySerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductInventorySerializer(product)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Product data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductInventorySerializer(product, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Product data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

class ProductVariantsAllView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductVariantsSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductVariantsSerializer(product)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Product data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductVariantsSerializer(product, many=True)
            return Response({
                 'status':status.HTTP_200_OK,
                 'message': 'Product data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

class AdditionalInfoAllView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = AdditionalInfoSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product  = Product.objects.get(product_id=_id)
                serializer = AdditionalInfoSerializer(product)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Product data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except  Product.DoesNotExist:
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = AdditionalInfoSerializer(product, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Product data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        
class SeoInfoAllView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductSeoSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductSeoSerializer(product)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Product data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                'message':'Product id not found'
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductSeoSerializer(product, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Product data retrieved successfully',
                 'data': serializer.data,
            }, status=200)


# update category in bulks  
class UpdateCategoriesInBulk(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = UpdateCategoryBrandInBulkSerializer
    def patch (self,request,format=None):
        
        # cid = request.query_paramss.get('category_id')
        cid = request.data.get('id')
        print(cid)
        
        try:
            category = Category.objects.get(category_id=cid)
        except Category.DoesNotExist:
            return Response(
                {
                    'status': 'error',
                    'message': "Category not found",
                },
                status=404
            )
        serializer = UpdateCategoryBrandInBulkSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        products = serializer.data.get('product_id')
        if not products:
            return Response(
                {
                    'status': 'error',
                    'message': "No products provided",
                },
                status=400
            )

        for product_id in products:
            try:
                product = Product.objects.get(product_id=product_id)
                product.category = category
                product.save()
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': 'error',
                        'message': f"No product found with this product id: {product_id}",
                    },
                    status=404
                )

        return Response(
            {
                'status': 'success',
                'message': "Category updated successfully for all products ",
            },
            status=200
        )
# update brands in bulks
class UpdateBrandsInBulk(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = UpdateCategoryBrandInBulkSerializer
    def patch (self,request,format=None):
        _id = request.data.get('id')
        try:
            brand = Brand.objects.get(brand_id=_id)
        except Brand.DoesNotExist:
            return Response(
                {
                    'status': 'error',
                    'message': "Brand not found",
                },
                status=404
            )
        serializer = UpdateCategoryBrandInBulkSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        products = serializer.data.get('product_id')
        if not products:
            return Response(
                {
                    'status': 'error',
                    'message': "No products provided",
                },
                status=400
            )

        for product_id in products:
            try:
                product = Product.objects.get(product_id=product_id)
                product.brand_id = brand
                product.save()
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': 'error',
                        'message': f"No product found with this product id: {product_id}",
                    },
                    status=404
                )

        return Response(
            {
                'status': 'success',
                'message': "Brand updated successfully for all products ",
            },
            status=200
        )
# update status in bulks
class UpdateStatusInBulk(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = UpdateStatusIsFeaturedSerializer
    def patch (self,request,format=None):
        status = request.data.get('status')
        if status is None:
            return Response(
                {
                    'status': 'error',
                    'message': "No Status provided",
                },
                status=400
            )
        serializer = UpdateStatusIsFeaturedSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        products = serializer.data.get('product_id')
        if not products:
            return Response(
                {
                    'status': 'error',
                    'message': "No products provided",
                },
                status=400
            )

        for product_id in products:
            try:
                product = Product.objects.get(product_id=product_id)
                product.availability = status
                product.save()
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': 'error',
                        'message': f"No product found with this product id: {product_id}",
                    },
                    status=404
                )
        return Response(
            {
                'status': 'success',
                'message': "Status updated successfully for all products ",
            },
            status=200
        )

# update created at in bulks
class UpdateCreatedAtInBulk(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = UpdateCreatedAtSerializer
    def patch (self,request,format=None):
        created_at= request.data.get('created_at')
        if created_at is None:
            return Response(
                {
                    'status': 'error',
                    'message': "No createdAt provided",
                },
                status=400
            )
        serializer = UpdateCreatedAtSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        products = serializer.data.get('product_id')
        if not products:
            return Response(
                {
                    'status': 'error',
                    'message': "No products provided",
                },
                status=400
            )
        for product_id in products:
            try:
                product = Product.objects.get(product_id=product_id)
                product.created_at = created_at
                product.save()
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': 'error',
                        'message': f"No product found with this product id: {product_id}",
                    },
                    status=404
                )
        return Response(
            {
                'status': 'success',
                'message': "createdAt updated successfully for all products ",
            },
            status=200
        )
# update is featured in bulkd
class UpdateIsFeaturedInBulk(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = UpdateStatusIsFeaturedSerializer
    def patch (self,request,format=None):
        is_featured = request.data.get('status')
        if is_featured is None:
            return Response(
                {
                    'status': 'error',
                    'message': "No isFeatured provided",
                },
                status=400
            )
        serializer = UpdateStatusIsFeaturedSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        products = serializer.data.get('product_id')
        if not products:
            return Response(
                {
                    'status': 'error',
                    'message': "No products provided",
                },
                status=400
            )

        for product_id in products:
            try:
                product = Product.objects.get(product_id=product_id)
                product.is_featured = is_featured
                product.save()
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': 'error',
                        'message': f"No product found with this product id: {product_id}",
                    },
                    status=404
                )

        return Response(
            {
                'status': 'success',
                'message': "isFeatured updated successfully for all products ",
            },
            status=200
        )

class DeleteProductInBulkView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def delete(self, request, format=None):
       
        product_id = request.data.get('product_id')
        print(type (product_id))

        if not product_id:
            return Response(
                {
                    'status': 'error',
                    'message': "No product id provided",
                },
                status=400
            )
        
        for _id in product_id: 
            try:
                product = Product.objects.get(product_id=_id)
                product.delete()
            except Product.DoesNotExist:
                return Response(
                    {
                        'status': 'error',
                        'message': f"No product found with this product id: {product_id}",
                    },
                    status=404
                )
         
        return Response({
            'status': status.HTTP_200_OK,
             'message': 'Product Deleted Successfully' 
            },
            status=200)  

class ProductIdView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductIdSerializer
    def post(self, request, format=None):
        serializer = ProductIdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_ids = serializer.data.get('product_id')
        print(product_ids)
        

        response_data = []
        for _id in product_ids: 
            try:
                product = Product.objects.get(product_id=_id)
                print(product.image.url)
                response_data.append({
                    
                    "product_id": product.product_id,
                    "product_name": product.name,
                    "product_image":product.image.url,
                    "product_price": product.price,
                    "product_size": product.size_variant,
                    "product_surface_finish": product.surface_finish,
                    "product_discount_price": product.discount_price,
                    "product_discount": product.discount,
                    "product_no_of_pieces_box": product.no_of_pcs_box,
                    "product_description": product.description,
                    "product_category":product.category.category_name,
                    "product_color":product.color,
                    "product_material":product.material,
                    "product_brand":product.brand.brand_name,
                    "product_min_quantity":product.min_order_quantity
                })
            except Product.DoesNotExist:
                response_data.append({
                    'product_id': _id,
                    'error': f"No product found with this product id: {_id}",
                })

        return Response({
            'product': response_data,
        })