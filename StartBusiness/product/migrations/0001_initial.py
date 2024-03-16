
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('sku', models.CharField(default='YRI68958', max_length=8, unique=True)),
                ('country_of_origin', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='product_images/')),
                ('demo_video', models.FileField(null=True, upload_to='product_videos/')),
                ('dimensions', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=2, max_digits=10), null=True, size=3)),
                ('color', models.CharField(blank=True, max_length=100)),
                ('material', models.CharField(blank=True, max_length=100)),
                ('style_design', models.CharField(blank=True, max_length=100)),
                ('surface_finish', models.CharField(blank=True, max_length=100)),
                ('edge_type', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('offer', models.CharField(blank=True, max_length=255)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('special_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('special_price_start', models.DateTimeField(auto_now=True)),
                ('special_price_end', models.DateTimeField(auto_now=True)),
                ('bulk_quantity_pricing', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('min_order_quantity', models.PositiveIntegerField(null=True)),
                ('bulk_discount', models.PositiveIntegerField(default=0)),
                ('tax_rate', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('tax_code', models.CharField(blank=True, max_length=20)),
                ('tax_exempt', models.BooleanField(default=False)),
                ('stock_quantity', models.PositiveIntegerField(null=True)),
                ('availability', models.BooleanField(default=True)),
                ('inventory_management', models.CharField(blank=True, max_length=20)),
                ('size_variant', models.CharField(blank=True, max_length=100)),
                ('color_variant', models.CharField(blank=True, max_length=100)),
                ('style_variant', models.CharField(blank=True, max_length=100)),
                ('application_details', models.TextField()),
                ('maintainance_details', models.TextField()),
                ('privacy_policy', models.TextField()),
                ('product_url', models.URLField()),
                ('meta_title', models.CharField(blank=True, max_length=255)),
                ('meta_description', models.TextField()),
                ('targeted_keywords', models.CharField(blank=True, max_length=255)),
                ('long_tail_keywords', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
