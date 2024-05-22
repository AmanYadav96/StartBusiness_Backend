import uuid
from django.db import models
from product.models import Product
from user.models import User

# Create your models here.
class Wishlist(models.Model):
    wishlist_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User,default=uuid.uuid4,on_delete=models.CASCADE)

class WishlistItems(models.Model):
    wishlist_items_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    wishlist_id = models.ForeignKey(Wishlist,on_delete=models.CASCADE,default=uuid.uuid4)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,default=uuid.uuid4)