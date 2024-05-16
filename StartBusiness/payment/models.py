import uuid
from django.db import models
import uuid
from user.models import User
from order.models import Order

# Create your models here.
class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, unique=True,null=True)
    status = models.CharField(max_length=20, default='pending')
    timestamp_initiated = models.DateTimeField(auto_now_add=True)
    timestamp_completed = models.DateTimeField(null=True, blank=True)
    user_mobile_no = models.CharField(max_length=10)
    user_email = models.EmailField(max_length=225,null=True)

