from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('pwm_item_api.core.urls')),
]