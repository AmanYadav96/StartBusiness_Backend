from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from address.models import Address
from address.serializers import AddressSerializer
from user.customepermission import IsCustomer
from rest_framework.permissions import IsAuthenticated

# add address
class AddressAddView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsCustomer]
    serializer_class = AddressSerializer
    def post(self, request,format=None):
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address = serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            "msg":'address added successfully',
            'address_id':address.address_id
        },status=201)


# update address
class AddressUpdateView(GenericAPIView):
    permission_classes = [IsAuthenticated,IsCustomer]
    serializer_class = AddressSerializer
    def patch(self, request, input):
        id = input
        try:
           address = Address.objects.get(address_id=id)
           serializer = AddressSerializer(address, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Address Updated Successfully'  
                },status=200)
        except Address.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid address_id',
                },
                status=404)

# get address or get address by id   
class AddressView(APIView):
    permission_classes = [IsAuthenticated,IsCustomer]
    serializer_class = AddressSerializer
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                address  = Address.objects.get(address_id=_id)
                serializer = AddressSerializer(address)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'address data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Address.DoesNotExist:
                return Response(
                    {
                        'status':  status.HTTP_404_NOT_FOUND,
                        'message': "address data not found",
                    },
                    status=404
                )
        else:
            address = Address.objects.all()
            serializer = AddressSerializer(address, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'address data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

# delete address
class AddressDeleteView(APIView):
    permission_classes = [IsAuthenticated,IsCustomer]
    def delete(self, request, input):
        try:
            id = input
            address = Address.objects.get(address_id=id)
            address.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'address Deleted Successfully'
            },status=200)
        except Address.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid address_id'
            }, status=status.HTTP_404_NOT_FOUND)

class AddressViewByUserId(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer
    def get(self, request, user_id):
       try:
            _id = user_id
            address = Address.objects.filter(user=_id)
            serializer = AddressSerializer(address, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'address retrieved Successfully',
                'data':serializer.data
            },status=200)
       except Address.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid user_id'
            }, status=status.HTTP_404_NOT_FOUND)


