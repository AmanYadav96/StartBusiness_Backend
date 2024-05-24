from rest_framework import generics
from contractor.serializers import ContractorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Contractor
# Create your  views here.
from rest_framework.permissions import IsAuthenticated
from user.customepermission import IsAdmin

class ContractorRegistorView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    
    serializer_class = ContractorSerializer
    #Creating
    def post(self, request,format=None):
        serializer = ContractorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'Contractor Registered',
            'data': serializer.data
        })

    #FindAll
class ContractorView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request, input = None,format=None):
        id = input
        print(self)
        if id is not None:
            if Contractor.objects.filter(contractor_id=id).count() >=1:
                contrator = Contractor.objects.get(contractor_id=id)
                serializer = ContractorSerializer(contrator)
                return Response({
                    'status':status.HTTP_200_OK,
                    'message': "Contractor data retrived",
                    'data':serializer.data
                })
            else:
                return Response({
                   'status':status.HTTP_400_BAD_REQUEST,
                   'message': "Invalid Contractor id"
                })
        else:
            contractor = Contractor.objects.all()
            serializer = ContractorSerializer(contractor, many=True)
            return Response({
               'status':status.HTTP_200_OK,
               'message': "Contractor"+" data retrived",
                'data':serializer.data
            })
        
#Update
class ContractorUpdateView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ContractorSerializer
    def patch(self, request, input, format=None):
        id = input
        if Contractor.objects.filter(contractor_id=id).count() >= 1:
            contrator = Contractor.objects.get(contractor_id=id)
            serializer = ContractorSerializer(contrator, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
           
            return Response({
              'status': status.HTTP_200_OK,
                'data': serializer.data,
               'message': 'Contractor Updated Successfully' 
            })
        else:
            return Response({
               'status': status.HTTP_400_BAD_REQUEST,
               'message': 'invalid id',
            })
#delete
class ContratorDeleteView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def delete(self, request, input):
        id = input
        print(self)
        if Contractor.objects.filter(contractor_id=id).count() >= 1:
            contrator = Contractor.objects.get(contractor_id=id)
            contrator.delete()
            return Response({
             'status': status.HTTP_200_OK,
              'message': 'Contractor Deleted Successfully' 
            })
        else:
            return Response({
              'status': status.HTTP_400_BAD_REQUEST,
              'message': 'invalid id',
            })