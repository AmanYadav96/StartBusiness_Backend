# Generated by Django 4.1.12 on 2024-02-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default=None, max_length=225),
        ),
    ]
