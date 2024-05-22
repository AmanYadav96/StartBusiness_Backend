import uuid
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView
from product_highlight.filter import ProductHighlightFilter
from product.models import Product
from product.serializers import ProductCartSerializer
from product_highlight.models import ProductHighlight
from product_highlight.serializers import ProductHighlightSerializer
from user.customepermission import IsAdmin
from rest_framework.permissions import IsAuthenticated,AllowAny


# add product highlight
class ProductHighlightAddView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductHighlightSerializer
    def post(self, request,format=None):
        serializer = ProductHighlightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Product Highlight Registered'
        },status=201)


# update product highlight
class ProductHighlightUpdateView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ProductHighlightSerializer
    def patch(self, request, input, format=None):
        id = input
        try:
           product_highlight = ProductHighlight.objects.get(product=id)
           serializer = ProductHighlightSerializer(product_highlight, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()

           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Product Highlight Updated Successfully'
                },status=200)
        except ProductHighlight.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid_id',
                },
                status=404)

# get product highlight   
class ProductHighlightAllView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductCartSerializer
    filterset_class = ProductHighlightFilter
    def list(self, request, *args, **kwargs):
        category_ids_str = request.query_params.get('category_ids', '')
        category_ids = []
        for category_id in category_ids_str.split(','):
            try:
                category_uuid = uuid.UUID(category_id.strip())
                category_ids.append(category_uuid)
            except ValueError:
                pass
        response = super().list(request, *args, **kwargs)
        best_seller = request.query_params.get('best_seller','')
        if best_seller=='true':
            if category_ids:
                print(category_ids)
                queryset = Product.objects.filter(producthighlight__best_seller=True,category__in=category_ids).distinct()
                serializer = self.get_serializer(queryset, many=True)
                data = serializer.data
                return Response({
                'status': 200,
                'message': 'Products filtered by category IDs successfully.',
                'data': data
                }, status=200)
            return Response({
                'status':status.HTTP_200_OK,
                'message':'product highlight data retrieved successfully ',
                'data':response.data
            },status=200)
        return Response({
                'status':status.HTTP_200_OK,
                'message':'product highlight data retrieved successfully ',
                'data':response.data
            },status=200)
    
#  get product highlight by id 
class ProductHighlightView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ProductHighlightSerializer
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        try:
            product_highlight  = ProductHighlight.objects.get(product=_id)
            serializer = ProductHighlightSerializer(product_highlight)
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'product_highlight data retrieved successfully',
                    'data': serializer.data,
                }, status=200
            )
        except ProductHighlight.DoesNotExist:
            return Response(
                {
                    'status':  status.HTTP_404_NOT_FOUND,
                    'message': "Product highlight not found",
                },
                status=404
            )

           
        

# delete product highlight
class ProductHighlightDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def delete(self, request, input):
        try:
            id = input
            product_highlight = ProductHighlight.objects.get(product_highlight_id=id)
            product_highlight.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Product Highlight Deleted Successfully'
            })
        except ProductHighlight.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid product_highlight_id'
            }, status=404)