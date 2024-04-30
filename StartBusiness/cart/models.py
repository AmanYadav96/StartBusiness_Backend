import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from product.models import Product
from user.models import User

class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, default=uuid.uuid4, on_delete=models.CASCADE)

    
class CartItem(models.Model):
    cart_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    quantity = models.PositiveIntegerField(default=1) 
    count = models.PositiveBigIntegerField(default=0)
    total_amount = models.PositiveBigIntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 