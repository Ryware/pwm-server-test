# Generated by Django 5.0.6 on 2024-07-08 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('method', models.CharField(max_length=100)),
                ('estimated_delivery', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('in_stock', models.BooleanField(default=True)),
                ('image', models.CharField(max_length=100)),
                ('review', models.DecimalField(decimal_places=1, max_digits=2)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('shipping', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='core.shipping')),
            ],
        ),
    ]
