from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year_published',
        'primary_publisher',
        'msrp',
        'price',
        'image_url',
    )

    ordering = (
        'name',
    )

    

admin.site.register(Product, ProductAdmin)