from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField
from product.models import Product
from user.models import User
# Create your models here.

class Compare(models.Model):
    compare_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)



class CompareItem(models.Model):
    compare_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    compare_id = models.ForeignKey(Compare,on_delete=models.CASCADE,default=uuid.uuid4)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,default=uuid.uuid4)
