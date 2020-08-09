import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.model import Product


class Order(models.Model):

    order_number = models.Charfield(max_length=32, null=False, editable=False)
    full_name = models.Charfield(max_length=50, null=False, blank=False)
    email = models.Emailfield(max_length=254, null=False, blank=False)
    phone_number = models.Charfield(max_length=20, null=False, blank=False)
    country = models.Charfield(max_length=40, null=False, blank=False)
    postcode = models.Charfield(max_length=20, null=True, blank=True)
    town_or_city = models.Charfield(max_length=40, null=False, blank=False)
    street_address1 = models.Charfield(max_length=80, null=False, blank=False)
    street_address2 = models.Charfield(max_length=80, null=False, blank=True)
    county = models.Charfield(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Uses UUID to generate a random unique order number
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Save override that sets the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    