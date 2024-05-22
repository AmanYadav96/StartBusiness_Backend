from rest_framework.generics import GenericAPIView,ListAPIView
from dealer.filter import DealerFilter
from dealer.models import Dealer
from dealer.serializers import DealerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from StartBusiness.s3_image_config import delete_file, upload_base64_file
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from user.customepermission import IsAdmin



# add dealer
class DealerAddView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = DealerSerializer
    def post(self , request):
            serializer = DealerSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
         
            return Response({
            "status" :"success",
            "message":"Dealer is added successfully",
            }, status=201
            )

# get all dealer and get one dealer by id
class DealerAllView(ListAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    queryset = Dealer.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = DealerSerializer
    filterset_class = DealerFilter
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if response.data == []:
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                "message":"No Data Found!!"
            })
        return Response({
            'status':status.HTTP_200_OK,
            "message":'dealer data retrieved successfully',
            'data':response.data
        },status=200)

# get one dealer by id
class DealerView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request, input=None, format=None):
            _id = input
            try:
                dealer  = Dealer.objects.get(dealer_id=_id)
                serializer = DealerSerializer(dealer)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': "dealer " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Dealer.DoesNotExist:
                return Response(
                    {
                        'status':  status.HTTP_404_NOT_FOUND,
                        'message': "dealer not found",
                    },
                    status=404
                )   

# update dealer
class UpdateDealerView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = DealerSerializer
    def patch(self, request, input, format=None):
      _id = input
      try:
            print(_id)
            dealer = Dealer.objects.get(dealer_id=_id)
            serializer = DealerSerializer(dealer, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
             'status': status.HTTP_200_OK,
             'message': "Dealer updated successfully"
        },status=200)
      except Dealer.DoesNotExist:
            return Response({
                 'status': status.HTTP_404_NOT_FOUND,
                'message':'Dealer id not found'
        },status=404)
     
       
# delete dealer
class DeleteDealerView(APIView):
     permission_classes = [IsAuthenticated,IsAdmin]
     def delete(self, request, input, format=None):
        _id = input
        try:
            dealer = Dealer.objects.get(dealer_id=_id)
            # file = dealer.dealer_image
            # file = file.name
            # delete_file(file)
            dealer.delete()
            return Response({
            'status': status.HTTP_200_OK,
             'message': 'Dealer Deleted Successfully' 
            },
            status=200)
        except Dealer.DoesNotExist:
            return Response({
             'status': status.HTTP_404_NOT_FOUND,
             'message': 'invalid dealer_id',
            },
            status=404)
    
    



 