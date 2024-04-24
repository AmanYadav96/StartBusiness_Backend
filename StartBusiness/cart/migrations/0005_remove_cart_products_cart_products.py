# Generated by Django 4.1.12 on 2024-04-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_sku'),
        ('cart', '0004_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='product.product'),
        ),
    ]
