from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField
class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=225,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category_image = models.ImageField(upload_to='category/',null=True)  # Image Field to store image of the product in base
    
class SubCategory(models.Model):
    sub_category = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE,null=True,blank=True,default=uuid.uuid4)
    subcategory_name = models.CharField(max_length=255)
    