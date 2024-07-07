from django.contrib import admin
from django.urls import path
from .views import ItemsView

urlpatterns = [
    path('api/items/', ItemsView.as_view(), name='items'),
]
