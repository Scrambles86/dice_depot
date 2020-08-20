from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ View that displays all available games from the json file """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
