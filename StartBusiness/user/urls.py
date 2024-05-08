from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'user register'),
    path('view/', UserView.as_view(), name = 'user view'),
    path('view/<uuid:input>/', UserView.as_view(), name = 'user view by id'),
    path('update/<uuid:input>/', UserUpdateView.as_view(), name = 'user update'),
    path('login/', UserLoginView.as_view(), name = 'user login'),
    path('otp-verification/<uuid:input>/', UserOtpVerificationEmail.as_view(), name = 'user view by id'),
    path('forgetPassword/<uuid:input>/', ForgetPassword.as_view(), name = 'forget Password view'),
    path('forgetPassword/', ForgetPassword.as_view(), name = 'forget Password view'),
    path('otp-resend/', UserOtpResend.as_view(), name = 'otp resend by email  id'),
    path('otp-resend/<uuid:input>/', UserOtpResend.as_view(), name = 'otp resend by email  id'),
    path('delete/<uuid:input>/',UserDeleteView.as_view(),name='user delete'),
  
]