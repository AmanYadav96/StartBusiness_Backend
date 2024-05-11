import random
import string
from django.db import models
import uuid
from category.models import Category
from product.models import Product

# Create your models here.

class Stock(models.Model):
    stock_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    current_stock = models.PositiveBigIntegerField(blank=True,null=True)
    unit = models.PositiveBigIntegerField(blank=True,null=True)
    default_price = models.FloatField(blank=True,null=True)
    regular_selling_price = models.FloatField(blank=True,null=True)
    regular_buying_price = models.FloatField(blank=True,null=True)
    mrp = models.FloatField(blank=True,null=True)
    stock_status = models.BooleanField(default=False)
    revenue = models.PositiveBigIntegerField(blank=True,null=True)
    sales = models.PositiveBigIntegerField(blank=True,null=True)
    minimum_stock_level = models.PositiveBigIntegerField(blank=True,null=True)
    maximum_stock_level = models.PositiveBigIntegerField(blank=True,null=True)
    dealer_price = models.PositiveBigIntegerField(blank=True,null=True)
    hsn_code = models.CharField(max_length=8,default=''.join(random.choices(string.ascii_uppercase, k=3))+''.join(random.choices(string.digits, k=5)),editable=False)
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE,default=uuid.uuid4)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,default=uuid.uuid4) 


    


