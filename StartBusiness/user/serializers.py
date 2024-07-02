from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('otp_key','created_at','password','last_login')


class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='user_mobile_number')
    class Meta:
       
        model = User
        fields = ('id','user_password')


class UserOtpSerializer(serializers.ModelSerializer):
     otp = serializers.CharField(source='otp_key')
     class Meta:
        model = User
        fields = ['otp']


class ForgetPasswordSerializer(serializers.ModelSerializer):
     password = serializers.CharField(source='user_password')
     class Meta:
        model = User
        fields = ['password']

