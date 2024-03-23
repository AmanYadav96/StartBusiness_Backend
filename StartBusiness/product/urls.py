from django.urls import path, include
from product.views import *

urlpatterns = [
    path('basicDetails/add/', ProductRegisterView.as_view(),name="add"),
    path('view/', ProductAllView.as_view(), name = 'product view'),
    path('view/<uuid:input>/', ProductView.as_view(), name = 'product view by id'),
    path('basicDetails/update/<uuid:input>/',UpdateProductView.as_view(),name="update product by id"),
    path('delete/<uuid:input>/',DeleteProductView.as_view() ,name='delete product by id'),
    path('media/update/<uuid:input>/',ProductMediaView.as_view(),name='update product visuals by product id'),
    path('productDetails/update/<uuid:input>/',ProductDetailsView.as_view(),name="product details update"),
    path('productPricing/update/<uuid:input>/',PricingView.as_view(),name="pricing update"),
    path('inventory/update/<uuid:input>/',InventoryView.as_view(),name='update inventory'),
    path('variant/update/<uuid:input>/',ProductVariantsView.as_view(),name="variants update"),
    path('additionalInfo/update/<uuid:input>/',ProductAdditionalView.as_view(),name="additional info update"),
    path('seoInfo/update/<uuid:input>/',SeoInformationView.as_view(),name="SEO info update"),
    path('basicDetails/view/',BasicProductAllView.as_view(),name="get all basic products"),
    path('basicDetails/view/<uuid:input>/',BasicProductAllView.as_view(),name="basic product by id"),
    path('media/view/',ProductMediaAllView.as_view(),name="get all media"),
    path('media/view/<uuid:input>/',ProductMediaAllView.as_view(),name='get media by id'),
    path('productDetails/view/',OtherDetailsAllView.as_view(),name="get other Details for all products"),
    path('productDetails/view/<uuid:input>/',OtherDetailsAllView.as_view(),name="product details view by id"),
    path('productPricing/view/',PricingAllView.as_view(),name="get all pricing"),
    path('productPricing/view/<uuid:input>/',PricingAllView.as_view(),name="get pricing by id"),
    path('inventory/view/',ProductInventoryAllView.as_view(),name='get all inventory'),
    path('inventory/view/<uuid:input>/',ProductInventoryAllView.as_view(),name='get inventory by id'),
    path('variant/view/',ProductVariantsAllView.as_view(),name="get all product variants"),
    path('variant/view/<uuid:input>/',ProductVariantsAllView.as_view(),name="get product variant by id"),
    path('additionalInfo/view/',AdditionalInfoAllView.as_view(),name="get all additional info"),
    path('additionalInfo/view/<uuid:input>/',AdditionalInfoAllView.as_view(),name="get additional info by id"),
    path('seoInfo/view/',SeoInfoAllView.as_view(),name="get all SEO info"),
    path('seoInfo/view/<uuid:input>/',SeoInfoAllView.as_view(),name="get SEO info by id") 
]