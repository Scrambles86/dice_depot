from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from bag.contents import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error.request, "Your bag is empty"
        return redirect(reverse('products'))

    user_bag = bag_contents(request)
    total = user_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
        'stripe_public_key': 'pk_test_51H0qbCAyzNETnnX7lIUBptAAA6ElAnwIfIqHIdw6SxeVULCxlKSAnM9JesnorroRI3R8fqtCuANbgoa3zLbm6oMf00PxDyzu87',
    }

    return render(request, template, context)
