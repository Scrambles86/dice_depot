from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ View that displays all available games from the json file """

    products = Product.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You need to type something first!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_description(request):
    """ View that displays all available games from the json file """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'products': product,
    }

    return render(request, 'products/products.html', context)
