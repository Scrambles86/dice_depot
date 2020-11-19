from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ Renders customers bag contents page """
    return render(request, 'bag/bag.html')

def add_item(request, product_id):
    """
    Add game to bag in chosen quantity
    """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag 
    return redirect(redirect_url)

def edit_bag(request, product_id):
    """
    Amend game quantity in bag
    """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
    else:
        bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(reverse, ('view_bag'))

def remove_from_bag(request, product_id):
    """
    Delete game from bag
    """

    bag = request.session.get('bag', {})

    bag.pop(product_id)

    request.session['bag'] = bag
    return HttpResponse(status=200)
