# Generated by Django 4.1.12 on 2024-02-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default=None, upload_to='category/'),
        ),
    ]
