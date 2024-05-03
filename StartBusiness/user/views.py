from sys import argv
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from compare.models import Compare
from cart.models import Cart
from user.serializers import UserLoginSerializer, UserSerializer,UserOtpSerializer,ForgetPasswordSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password , check_password
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import random
from datetime import datetime, timezone
import json
from .customepermission import IsManager
from rest_framework.permissions import IsAuthenticated
# from StartBusiness.email import send_verification_email
from .tasks import send_verification_email


# basic used functions ......

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }


def otp_generator(id):
   otp = random.randint(1000, 9999)
   d = json.dumps({'otp': otp, 'timestamp': datetime.now().strftime('%H:%M:%S')})
   user = User.objects.get(user_email=id)
   user.otp_key = d
   user.save()
   send_verification_email.delay(otp, id)
  



def time_difference(start_time, end_time, time_format='%H:%M:%S'):
    start = datetime.strptime(start_time, time_format)
    end = datetime.strptime(end_time, time_format)
    time_diff = end - start
    return time_diff.seconds/60

async def create(user_id):
     cart = Cart.objects.create(user_id=user_id)
     cart.save()
     compare = Compare.objects.create(user_id = user_id)
     compare.save()
# views code .................

# User register view --------------------------------
class UserRegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request , format=None):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.validated_data['user_password']=make_password(serializer.validated_data['user_password'])
        serializer.save()
        if serializer.data['user_role'] == 'Customer':
            create(serializer.data['user_id'])
        id = request.data.get('user_email')
        otp_generator(id)
        return Response({
                 'status': status.HTTP_201_CREATED,
                 'message': " User Successfully registered",
                 'user_id': serializer.data['user_id']
                                   },status=201)

      
# User Otp-verification view----------------------------------------------------------------
        
class UserOtpVerificationEmail(GenericAPIView):
    serializer_class = UserOtpSerializer
    def post(self, request,input= None, format=None):
        id = input
        user =  User.objects.get(user_id=id)
        new_dict = {}
        new_dict =json.loads(user.otp_key)
        first_time =new_dict.get('timestamp')
        second_time = datetime.now().strftime('%H:%M:%S')
        timed = time_difference(first_time,second_time)
        otp1 = int(request.data.get('otp'))
        otp2 = int(new_dict.get('otp'))
        if(timed < 10.0):
            if(otp1==otp2):
                user.is_verify = True
                user.save()
                return Response({
                    'status': status.HTTP_200_OK,
                    "message":"user is verified"
                },status=200)
            else:
                Response.status_code = status.HTTP_400_BAD_REQUEST
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    "message":"invalid otp"
                },status=400)
        else:
        
         return Response({
         'status_code': status.HTTP_400_BAD_REQUEST  ,
         "message":"otp expired"
         },status=400)

        
# User otp-resend view----------------------------------------------------------------
class UserOtpResend(APIView):
    
    def get(self, request,input=None,format=None):
      id = input
      email_id = ""
      user_iddd = ""
      if  id is not None:
       if User.objects.filter(user_id=id).count()>=1:
           user = User.objects.get(user_id=id)
           email_id = user.user_email
           user_iddd =  otp_generator(email_id)
           return Response({
            'status_code': status.HTTP_200_OK,
            'message':"otp sent successfully",
            'user_id':user_iddd},status=200)
       else:
             return Response({
              'status':status.HTTP_200_OK,
              'message':'user is not registered with this id'
          })
       
      elif request.query_params.get('email_id') is not None:
        if User.objects.filter(user_email=request.query_params.get('email_id')).count()>=1:
          email_id = request.query_params.get('email_id')
          user_iddd =  otp_generator(email_id)
          return Response({
            'status_code': status.HTTP_200_OK,
            'message':"otp sent successfully",
            'user_id':user_iddd
          },status=200)
        else:
         return Response({
              'status':status.HTTP_400_BAD_REQUEST,
              'message':'user is not registered with this id'
          },status=400)
        
      else:  
          return Response({
              'status':status.HTTP_400_BAD_REQUEST,
              'message':'user is not registered with this id'
          },status=400)
      
        
        


# User getall user View----------------------------------------------------------------


class ForgetPassword(GenericAPIView):
     serializer_class = ForgetPasswordSerializer
     def post (self, request,input=None,format=None):
       
       id = request.query_params.get('email_id')
       if id is not None:
            user = User.objects.get(user_email=id)
            
            serializer = ForgetPasswordSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception = True)
            serializer.validated_data['user_password']=make_password(serializer.validated_data['user_password'])
            serializer.save()

           
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Password Updated Successfully' 
                },status=200
            )
         
       else:
            
            return Response({
            'status code': status.HTTP_400_BAD_REQUEST,
            'message':"user is not registered with this email."         
               },status=400)

     

        


class UserView(APIView):
    # permission_classes = [IsManager]

    def get(self, request, input=None, format=None):
        id = input
        if id is not None:
            if User.objects.filter(user_id=id).count() >= 1:
                user  = User.objects.get(user_id=id)
                serializer = UserSerializer(user)
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': "user " + 'data retrieved successfully',
                        'data': serializer.data,
                    },status=200
                )
            else:
                return Response(
                    {
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': "Invalid user id",
                    },status=400
                )
        else:
            user = User.objects.all()    
            serializer = UserSerializer(user, many=True)
            return Response({
                 'status': status.HTTP_200_OK,
                 'message': "user " + 'data retrieved successfully',
                 'data': serializer.data,
            },status=200)
        

# user update view----------------------------------------------------------------
        
class UserUpdateView(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request, input, format=None):
        id = input
        if User.objects.filter(user_id=id).count() >= 1:
            user = User.objects.get(user_id=id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            if request.data.get('user_password') is not None:
             serializer.validated_data['user_password']=make_password(serializer.validated_data['user_password'])
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'user Updated Successfully' 
                },status=200
            )
        else:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'invalid id',
                },status=400
            )


# User login view----------------------------------------------------------------
class UserLoginView(GenericAPIView):
   serializer_class = UserLoginSerializer
   def post (self, request,format=None):
      id = request.data.get('id')
      password = request.data.get('user_password')
     
      if User.objects.filter(user_email=id).count() >= 1 or User.objects.filter(user_mobile_number=id).count()>=1:
        user =  User.objects.filter(user_email=id) or User.objects.filter(user_mobile_number=id)
        if user[0].is_verify is True:

       
         if(check_password(password,user[0].user_password)):
             token =get_tokens_for_user(user[0])
             cart = Cart.objects.get(user_id = user[0].user_id)
             compare = Compare.objects.filter(user_id = user[0].user_id)
             return Response({
              'status code': status.HTTP_200_OK,
              'message':"user logged in successfully",
              'user_id': user[0].user_id,
              'cart_id': cart.cart_id,
              'compare_id':compare[0].compare_id,
              'user_role': user[0].user_role,
              'token': token
                             },status=200)
         else:
             return Response({'status': status.HTTP_400_BAD_REQUEST,
                              'message':"invalid password"
                              },status=400)
             
        else:
                 otp_generator(user[0].user_email)
                 return Response({'status': status.HTTP_400_BAD_REQUEST,
                              'message':"user is not verified first verify yor account",
                              'is_verify': user[0].is_verify,
                              'user_id': user[0].user_id
                              },status=400)
      else:
        
          return Response({
              'status code': status.HTTP_400_BAD_REQUEST,
              'message':"user is not registered with this email or mobile number"         
               },status=400)
