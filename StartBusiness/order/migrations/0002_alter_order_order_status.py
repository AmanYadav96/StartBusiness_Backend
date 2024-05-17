# Generated by Django 5.0.4 on 2024-05-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Pending', editable=False, max_length=50),
        ),
    ]
