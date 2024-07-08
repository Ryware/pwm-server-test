from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Item


def item_list(request):
    items = Item.objects.all().values('id', 'name', 'price', 'currency', 'category', 'in_stock', 'image', 'review', 'discount', 'description', 'shipping__cost', 'shipping__method', 'shipping__estimated_delivery')
    items_list = list(items)
    return JsonResponse(items_list, safe=False)
