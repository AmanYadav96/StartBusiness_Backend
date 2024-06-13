import uuid
from django.db import models
from category.models import Category
from payment.models import Payment
from user.models import User
from product.models import Product


class Invoice(models.Model):
    invoice_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_number = models.CharField(blank=True,max_length=10,editable=False,default='SG11112212')
    billing_address = models.TextField(blank=True)
    invoice_status = models.CharField(blank=True,max_length=50,default='Unpaid')
    shipping_address=models.TextField(blank=True)
    invoice_image = models.FileField(upload_to='invoice/',editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0) 
    labour_cost = models.PositiveIntegerField(default=0)
    gst = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    payment_method = models.CharField(choices=(('Cash', 'Cash'),('Credit Card', 'Credit Card'),('Debit Card','Debit Card')),max_length=50,blank=True)
    customer_name = models.CharField(max_length=50,blank=True)
    customer_mobile_number = models.CharField(max_length=10,blank=True)
    customer_notes = models.TextField(blank=True)
    
class InvoiceItem(models.Model):
    invoice_item_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveBigIntegerField(default=0)
    discount_price = models.PositiveBigIntegerField(default=0)
    total_price = models.DecimalField(default=0,decimal_places=2,max_digits=10)
    invoice = models.ForeignKey(Invoice,related_name='items',default=uuid.uuid4,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,default=uuid.uuid4,on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category,default=uuid.uuid4,on_delete=models.CASCADE)