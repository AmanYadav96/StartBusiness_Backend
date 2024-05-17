# Generated by Django 5.0.4 on 2024-05-17 09:26

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_orderitem_delivery_charges_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_charges',
        ),
        migrations.RemoveField(
            model_name='order',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='delivery_charges',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='discount_price',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order'),
        ),
    ]
