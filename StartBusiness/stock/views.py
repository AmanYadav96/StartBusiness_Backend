from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from stock.models import Stock
from stock.serializers import StockSerializer
from user.customepermission import IsAdmin
from rest_framework.permissions import IsAuthenticated,AllowAny

# add stock
class StockAddView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = StockSerializer
    def post(self, request,format=None):
        serializer = StockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Stock added successfully'
        },status=201)


# update stock
class StockUpdateView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = StockSerializer
    def patch(self, request, input):
        _id = input
        try:
           stock = Stock.objects.get(stock_id=_id)
           serializer = StockSerializer(stock, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Stock Updated Successfully'  
                },status=200)
        except Stock.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid stock_id',
                },
                status=404)

# get stock or get stock by id   
class StockView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StockSerializer
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                stock  = Stock.objects.get(stock_id=_id)
                serializer = StockSerializer(stock)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'stock data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Stock.DoesNotExist:
                return Response(
                    {
                        'status':  status.HTTP_404_NOT_FOUND,
                        'message': "stock data not found",
                    },
                    status=404
                )
        else:
            stock = Stock.objects.all()
            serializer = StockSerializer(stock, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'stock data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

# delete stock
class StockDeleteView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def delete(self, request, input):
        try:
            _id = input
            stock = Stock.objects.get(stock_id=_id)
            stock.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Stock Deleted Successfully'
            },status=200)
        except Stock.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid stock_id'
            }, status=status.HTTP_404_NOT_FOUND)
