from rest_framework.response import Response
from rest_framework import generics
from manager.serializers import ManagerSerializer
from rest_framework.views import APIView
from manager.models  import Manager
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from user.customepermission import IsAdmin
class ManagerRegisterView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ManagerSerializer
    def post(self , request):
        serializer = ManagerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status" :"success",
            "message":"Manager is added successfully",
            }, status=201

        )
    
class ManagerView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            if Manager.objects.filter(manager_id=_id).count() > 0:
                manager  = Manager.objects.get(manager_id=_id)
                serializer = ManagerSerializer(manager)


                return Response(
                    {
                        'status': 'success',
                        'message': "user " + 'data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            else:
             
                return Response(
                    {
                        'status':  'error',
                        'message': "Manager not found",
                    },
                    status=404
                )
        else:
            manager = Manager.objects.all()    
            serializer = ManagerSerializer(manager, many=True)
            return Response({
                 'status': 'success',
                 'message': "manager " + 'data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
    

class UpdateManagerView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def patch(self, request, input, format=None):
        _id = input
        print(_id)
        manager = Manager.objects.get(manager_id=_id)
        serializer = ManagerSerializer(manager, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if _id is not None:
            serializer.save()
            return Response({
             'status': 'success',
             'message': "manager updated successfully"
        },status=200)
        else:
            return Response({
                'status':'manager id not found'
        },status=404)
     
       

class DeleteManagerView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def delete(self, request, input, format=None):
        _id = input
        manager = Manager.objects.get(manager_id=_id)
        if _id is not None:
            manager.delete()
            return Response({
            'status': 'success',
            'message': "manager deleted successfully"
        }, status=200)
        else:
            return Response({
                'status': 'failure',
                'message': "No such manager id exists for delete."
                }, status=404)
    

