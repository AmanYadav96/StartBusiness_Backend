# Generated by Django 5.0.4 on 2024-05-22 06:04

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('wishlist_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItems',
            fields=[
                ('wishlist_items_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('wishlist_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='wishlist.wishlist')),
            ],
        ),
    ]
