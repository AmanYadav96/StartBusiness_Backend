# Generated by Django 4.1.13 on 2024-02-08 07:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_alter_manager_manager_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='manager_id',
            field=models.UUIDField(default=uuid.UUID('f126c5bf-18b8-4f10-ab47-fc32f90b63eb'), editable=False, primary_key=True, serialize=False),
        ),
    ]
