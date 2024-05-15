import uuid
from django.db import models



class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    payment_method = models.CharField(max_length = 50, choices=(('UPI', 'UPI'),('CREDIT CARD', 'CREDIT CARD'),('DEBIT CARD', 'DEBIT CARD'),('NET BANKING', 'NET BANKING')),default='')
    payment_status = models.CharField(max_length = 50, choices=(('Paid', 'Paid'),('Unpaid', 'Unpaid')),default='Unpaid',editable=False)
    payment_date = models.DateTimeField(auto_now_add=True,editable=False)
    
