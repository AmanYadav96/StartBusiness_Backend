import uuid
from django.db import models
from product.models import Product
from address.models import Address
from user.models import User


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    order_status = models.CharField(max_length = 50, choices=(('Placed', 'Placed'),('Pending', 'Pending'),('Cancelled','Cancelled')),default='Placed',editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,default=uuid.uuid4,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,default=uuid.uuid4,on_delete=models.CASCADE)


class OrderItem(models.Model):
    order_item_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    order = models.ForeignKey(Order,default=uuid.uuid4,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,default=uuid.uuid4,on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0,editable=False)
    discount_price = models.PositiveBigIntegerField(default=0,editable=False)
    delivery_charges = models.PositiveIntegerField(default=0)
    total_price = models.PositiveBigIntegerField(default=0,editable=False)
    quantity = models.PositiveIntegerField(default=1)
