from rest_framework import serializers
from product.models import Product
from django.contrib.postgres.fields import ArrayField

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id','name','category','brand','country_of_origin','description','counter']

# class ProductVideoSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['name','description','category','brand','sku','country_of_origin']

# Serielizer for getting full details 
class ProductFullDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = ['image','image1','image2','image3','image4' ,'image5','demo_video','counter']


class ProductDetailsSerializer(serializers.ModelSerializer):
    layout = serializers.ListField(required=False, allow_empty=True)
    class Meta:
        model = Product 
        fields = ['length','length_unit','width','width_unit','thickness','thickness_unit','weight','weight_unit', 'color', 'material', 'style_design', 'surface_finish', 'edge_type','sq_ft_box', 'no_of_pcs_box','product_collections','label','layout','counter']


class ProductPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product       
        fields = ['price', 'discount','offer_type', 'discount_price','discount_price_start','discount_price_end','min_order_quantity','bulk_quantity_pricing','bulk_discount','tax_rate', 'hsn_code','counter' ]




class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['sku','minimum_stock_level', 'maximum_stock_level','availability','counter']


class ProductVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['size_variant', 'color_variant', 'style_variant','related_product','cross_selling_product','counter']

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_use','maintenance_details','privacy_policy','counter']


class ProductSeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_url','meta_title','meta_description','featured_keywords','long_tail_keywords','status','is_featured','counter']

class UpdateCategoryBrandInBulkSerializer(serializers.ModelSerializer):
    product_id = serializers.ListField()
    id = serializers.UUIDField(source='category')
    

    class Meta:
        model = Product
        fields = ['product_id','id']

class UpdateStatusIsFeaturedSerializer(serializers.ModelSerializer):
    product_id = serializers.ListField()
    status = serializers.BooleanField(source='availability')
    class Meta:
        model = Product
        fields = ['product_id','status']

class UpdateCreatedAtSerializer(serializers.ModelSerializer):
    product_id = serializers.ListField()
    created_at = serializers.DateTimeField()
    class Meta:
        model = Product
        fields=['product_id','created_at']


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id','brand','min_order_quantity','name','image','length','length_unit','width','width_unit','thickness','thickness_unit','weight','weight_unit','price','discount','discount_price','status','category']

class ProductIdSerializer(serializers.ModelSerializer):
    product_id = serializers.ListField()
    class Meta:
        model = Product
        fields = ['product_id']