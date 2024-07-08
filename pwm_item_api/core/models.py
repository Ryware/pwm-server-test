from django.db import models


class Shipping(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=100)
    estimated_delivery = models.CharField(max_length=100)


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    image = models.CharField(max_length=100)
    review = models.DecimalField(max_digits=2, decimal_places=1)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    shipping = models.OneToOneField(Shipping, on_delete=models.CASCADE, related_name='item')
