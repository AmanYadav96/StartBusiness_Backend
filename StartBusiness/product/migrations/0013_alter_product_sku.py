# Generated by Django 4.1.12 on 2024-04-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='DLT66155', max_length=8),
        ),
    ]
