# Generated by Django 5.0.4 on 2024-06-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_alter_stock_hsn_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='hsn_code',
            field=models.CharField(default='CSO72046', editable=False, max_length=8),
        ),
    ]
