import uuid
from django.db import models
from product.models import Product
from address.models import Address
from user.models import User



class OrderItem(models.Model):
    order_item_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    product = models.ForeignKey(Product,default=uuid.uuid4,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    order_amount = models.PositiveBigIntegerField(editable=False)
    order_status = models.CharField(max_length = 50, choices=(('Placed', 'Placed'),('Dispatched', 'Dispatched'),('Delivered', 'Delivered'),('Cancelled','Cancelled')),default='Placed')
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2,null=True,editable=False)
    payment_method = models.CharField(max_length = 50, choices=(('UPI', 'UPI'),('CREDIT CARD', 'CREDIT CARD'),('DEBIT CARD', 'DEBIT CARD'),('NET BANKING', 'NET BANKING')),default='')
    payment_status = models.CharField(max_length = 50, choices=(('Paid', 'Paid'),('Unpaid', 'Unpaid')),default='Unpaid')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length= 50)
    user = models.ForeignKey(User,default=uuid.uuid4,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,default=uuid.uuid4,on_delete=models.CASCADE)
    order_item = models.ManyToManyField(OrderItem)
    # product = models.ManyToManyField(Product)
