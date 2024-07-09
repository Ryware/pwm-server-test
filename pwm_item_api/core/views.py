from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Item


def item_list(request):
    items = Item.objects.all()
    items_list = []
    for item in items:
        item_data = {
            'id': item.id,
            'name': item.name,
            'price': float(item.price),
            'currency': item.currency,
            'category': item.category,
            'inStock': item.in_stock,
            'image': item.image,
            'review': float(item.review),
            'discount': float(item.discount),
            'description': item.description,
            'shipping': {
                'cost': float(item.shipping.cost),
                'method': item.shipping.method,
                'estimatedDelivery': item.shipping.estimated_delivery
            }
        }
        items_list.append(item_data)
    return JsonResponse(items_list, safe=False)
