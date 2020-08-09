from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_numnber', 'date', 
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_numnber', 'date', 'full_name', 
              'email', 'phone_number', 'country', 
              'postcode', 'town_or_city', 'street_address1', 
              'street_address2', 'county', 'delivery_cost',
               'order_total', 'grand_total',)

    list_display = ('order_numnber', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('-date',)
