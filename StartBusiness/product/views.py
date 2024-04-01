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
from brand.models import Brand
# register 01
class ProductRegisterView(GenericAPIView):
    serializer_class = ProductSerializer
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['counter'] = 1
        serializer.save()
       
        return Response({
            "status" :"success",
            "message":"Product is added successfully",
            "product_id":serializer.data['product_id'],
            # 'product_id':serializer
            }, status=201
  
        ) 


# View Product Full
class ProductAllView(ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [OrderingFilter, SearchFilter,DjangoFilterBackend]
    pagination_class = CustomPagination
    serializer_class = ProductFullDetailsSerializer
    search_fields = []
    filterset_class = ProductFilter
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        
        
        return Response({
            'status':status.HTTP_200_OK,
            "message":'product data retrieved successfully ',
            'data':response.data
        },status=200)
    

class ProductView(APIView):
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if Product.objects.filter(product_id=_id).count() > 0:
            product  = Product.objects.get(product_id=_id)
            serializer = ProductFullDetailsSerializer(product)
            return Response(
                {
                    'status': 'success',
                    'message': "Product data retrieved successfully",
                    'data': serializer.data,
                }, status=200
            )
        else:
             
            return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
        )
    
    

class UpdateProductView(APIView):
    serializer_class = ProductSerializer
    def patch(self, request, input, format=None):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)
    

class DeleteProductView(APIView):
    def delete(self, request, input, format=None):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            product = Product.objects.get(product_id=_id)
            product.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Product Deleted Successfully' 
            },
            status=200)
        else:
            return Response({
             'status': status.HTTP_400_BAD_REQUEST,
             'message': 'invalid product id',
            },
            status=400)
   
        

# Other ----------------------------------------------------------
        
 # Product update media
class ProductMediaView(GenericAPIView):
    serializer_class = ProductMediaSerializer
    def patch(self,request ,input):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductMediaSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 2
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)

# Product Details View
class ProductDetailsView(GenericAPIView):
    serializer_class = ProductDetailsSerializer
    def patch(self,request ,input):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductDetailsSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 3
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)



   # Pricing update
class PricingView(GenericAPIView):
    serializer_class = ProductPricingSerializer
    def patch(self,request ,input):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductPricingSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 4
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)
    # Product update inventory
class InventoryView(GenericAPIView):
    serializer_class = ProductInventorySerializer
    def patch(self,request ,input):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductInventorySerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 5
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)
    

    # Product Variants View
class ProductVariantsView(GenericAPIView):
    serializer_class = ProductVariantsSerializer
    def patch(self,request ,input):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductVariantsSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 6
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)

# Product additional information update
    
class ProductAdditionalView(GenericAPIView):
    serializer_class = AdditionalInfoSerializer
    def patch(self,request ,input):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = AdditionalInfoSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 7
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)

# Seo info  update 
        
class SeoInformationView(GenericAPIView):
    serializer_class = ProductSeoSerializer
    def patch(self,request ,input):
        _id = input
        if Product.objects.filter(product_id=_id).count() >= 1:
            print(_id)
            product = Product.objects.get(product_id=_id)
            serializer = ProductSeoSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['counter'] = 8
            serializer.save()
            return Response({
             'status': 'success',
             'message': "Product updated successfully"
        },status=200)
        else:
            return Response({
                'status':'Product id not found'
        },status=404)
       
    
    
# ---------------------------------------------------------------------
class BasicProductAllView(APIView):
    serializer_class = ProductSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductSerializer(product)
                return Response(
                    {
                        'status': 'success',
                        'message': "Product data retrieved successfully",
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductSerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "Product data retrieved successfully",
                 'data': serializer.data,
            }, status=200)


# media all view
class ProductMediaAllView(APIView):
    serializer_class = ProductMediaSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductMediaSerializer(product)
                return Response(
                    {
                        'status': 'success',
                        'message': "Product data retrieved successfully",
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductMediaSerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "Product data retrieved successfully",
                 'data': serializer.data,
            }, status=200)
        

# product details all view
class OtherDetailsAllView(APIView):
    serializer_class = ProductDetailsSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductDetailsSerializer(product)
                return Response(
                    {
                        'status': 'success',
                        'message': "Product data retrieved successfully",
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductDetailsSerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "Product data retrieved successfully",
                 'data': serializer.data,
            }, status=200)

# pricing all view
class PricingAllView(APIView):
    serializer_class = ProductPricingSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductPricingSerializer(product)
                return Response(
                    {
                        'status': 'success',
                        'message': "Product data retrieved successfully",
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductPricingSerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "Product data retrieved successfully",
                 'data': serializer.data,
            }, status=200)

# product tax view all

class ProductInventoryAllView(APIView):
    serializer_class = ProductInventorySerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductInventorySerializer(product)
                return Response(
                    {
                        'status': 'success',
                        'message': "Product data retrieved successfully",
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductInventorySerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "Product data retrieved successfully",
                 'data': serializer.data,
            }, status=200)
        

class ProductVariantsAllView(APIView):
    serializer_class = ProductVariantsSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductVariantsSerializer(product)
                return Response(
                    {
                        'status': 'success',
                        'message': "Product data retrieved successfully",
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductVariantsSerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "Product data retrieved successfully",
                 'data': serializer.data,
            }, status=200)
        

class AdditionalInfoAllView(APIView):
    serializer_class = AdditionalInfoSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = AdditionalInfoSerializer(product)
                return Response(
                    {
                        'status': 'success',
                        'message': "Product data retrieved successfully",
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = AdditionalInfoSerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "Product data retrieved successfully",
                 'data': serializer.data,
            }, status=200)
        
class SeoInfoAllView(APIView):
    serializer_class = ProductSeoSerializer
    def get(self, request, input=None,format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Product.objects.filter(product_id=_id).count() > 0:
                product  = Product.objects.get(product_id=_id)
                serializer = ProductSeoSerializer(product)
                return Response(
                    {
                        'status': 'success',
                        'message': "Product data retrieved successfully",
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Product not found",
                    },
                    status=404
                )
        else:
            product = Product.objects.all()    
            serializer = ProductSeoSerializer(product, many=True)
            return Response({
                 'status': 'success',
                 'message': "Product data retrieved successfully",
                 'data': serializer.data,
            }, status=200)


# update category in bulks  
class UpdateCategoriesInBulk(GenericAPIView):
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
   