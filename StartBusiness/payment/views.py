from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from payment.models import Payment
from rest_framework.generics import GenericAPIView
from payment.serializers import PaymentSerializer
# Create your views here.

class PaymentAddView(GenericAPIView):
        serializer_class = PaymentSerializer
        def post(self, request,format=None):
          serializer = PaymentSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response({
              'status':status.HTTP_201_CREATED,
              "msg":'Payment Created successfully',
              'data':serializer.data,
          },status=201)


class PaymentView(APIView):
    serializer_class = PaymentSerializer
    def get(self, request, input=None, format=None):
        _id = input
        print(_id)
        if _id is not None:
            try:
                payment  = Payment.objects.get(payment_id=_id)
                serializer = PaymentSerializer(payment)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Payment data retrieved successfully',
                        'data': serializer.data,
                    }, status=200
                )
            except Payment.DoesNotExist:
                return Response(
                    {
                        'status':  status.HTTP_404_NOT_FOUND,
                        'message': "invalid payment_id",
                    },
                    status=404
                )
        else:
            payment = Payment.objects.all()
            serializer = PaymentSerializer(payment, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': 'Payment data retrieved successfully',
                 'data': serializer.data,
            }, status=200)
        

class PaymentUpdateView(GenericAPIView):
    serializer_class = PaymentSerializer
    def patch(self, request, input):
        _id = input
        try:
           payment = Payment.objects.get(payment_id=_id)
           serializer = PaymentSerializer(payment, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({
                'status': status.HTTP_200_OK,
                'message': 'Payment Updated Successfully',
                'data': serializer.data
                },status=200)
        except payment.DoesNotExist:
            return Response({
               'status': status.HTTP_404_NOT_FOUND,
                'message': 'invalid payment_id',
                },
                status=404)

class PaymentDeleteView(APIView):
    def delete(self, request, input):
        try:
            _id = input
            order = Payment.objects.get(payment_id=_id)
            order.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Payment Deleted Successfully'
            },status=200)
        except Payment.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Invalid Payment_id'
            }, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
