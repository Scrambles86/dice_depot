from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year_published',
        'publishers',
        'price',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Product, ProductAdmin)