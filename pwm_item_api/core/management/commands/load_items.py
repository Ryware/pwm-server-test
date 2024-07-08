import json
from django.core.management.base import BaseCommand
from pwm_item_api.core.models import Item, Shipping

class Command(BaseCommand):
    help = 'Load items from JSON file'

    def handle(self, *args, **kwargs):
        with open('data.json', 'r') as file:
            data = json.load(file)
            for item_data in data:
                shipping_data = item_data.pop('shipping')
                # Transform the JSON key 'estimatedDelivery' to the model field 'estimated_delivery'
                shipping_data['estimated_delivery'] = shipping_data.pop('estimatedDelivery')
                shipping = Shipping.objects.create(**shipping_data)
                item_data['in_stock'] = item_data.pop('inStock')
                Item.objects.create(**item_data, shipping=shipping)
