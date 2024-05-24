from celery import shared_task
from product.models import Product
from rest_framework.response import Response
from rest_framework import status
@shared_task
def calculate_total_price(items):
    total_price = 0
    for item in items:
            product_id = item['product']
            quantity = item['quantity']
            print(product_id)
            try:
                product = Product.objects.get(product_id=product_id.product_id)
                total_price += product.price * quantity
            except Product.DoesNotExist:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': f'Product with id {product_id} does not exist.'
                    })
    return total_price


   