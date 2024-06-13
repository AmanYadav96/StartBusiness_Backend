# Generated by Django 5.0.4 on 2024-06-12 09:49

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=225)),
                ('mobile_number', models.CharField(max_length=225, unique=True)),
                ('pincode', models.CharField(blank=True, max_length=225)),
                ('locality', models.CharField(blank=True, max_length=225)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=225)),
                ('state', models.CharField(blank=True, max_length=225)),
                ('landmark', models.CharField(blank=True, max_length=225)),
                ('alternate_mobile_number', models.CharField(blank=True, max_length=225)),
                ('user', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
