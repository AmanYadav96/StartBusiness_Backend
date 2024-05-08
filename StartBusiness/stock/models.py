from django.db import models
import uuid
from category.models import Category
from product.models import Product

# Create your models here.

class Stock(models.Model):
    stock_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE,default=uuid.uuid4)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,default=uuid.uuid4) 
    current_stock = models.PositiveBigIntegerField(blank=True,null=True)
    unit = models.PositiveBigIntegerField(blank=True,null=True)
    default_price = models.FloatField(blank=True,null=True)
    regular_selling_price = models.FloatField(blank=True,null=True)
    regular_buying_price = models.FloatField(blank=True,null=True)
    mrp = models.FloatField(blank=True,null=True)
    stock_status = models.BooleanField(default=False)
    


