from rest_framework import serializers

from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id','amount','user','order','payment_method','transaction_id','status','timestamp_completed','user_mobile_no','user_email','link_id']