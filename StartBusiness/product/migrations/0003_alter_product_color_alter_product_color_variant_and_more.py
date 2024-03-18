# Generated by Django 4.1.12 on 2024-03-18 10:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_discount_price_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='color_variant',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='cross_selling_product',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='edge_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_keywords',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='related_product',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_variant',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='JKM49958', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft'), ('Pending', 'Pending')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='style_design',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='style_variant',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='surface_finish',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax_class',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
