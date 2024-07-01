import uuid
from django.db import models

from product.models import Product

class ProductHighlight(models.Model):
    product_highlight_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    flash_deal = models.BooleanField(default=False,blank=True)
    discount_date = models.DateField(null=True)
    hot_deals = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    top_rated = models.BooleanField(default=False)
    big_saving = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    update_key = models.BooleanField(default=True)
    product = models.OneToOneField(Product, default=uuid.uuid4, unique=True, on_delete=models.CASCADE)
    
