from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ View that displays all available games from the json file """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You need to type something first!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    sorted_by = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'sorted_by': sorted_by,
    }

    return render(request, 'products/products.html', context)


def product_description(request, product_id):
    """ View that displays the details for a single product """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product_description.html', context)

@login_required
def add_product(request):
    """ Add a new product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'That function is reserved for store admins')
        return redirect(reverse,('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added to database')
            
        else:
            messages.error(request, 'Add product failed - please check the fields are correct before submitting')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit existing products """

    if not request.user.is_superuser:
        messages.error(request, 'That function is reserved for store admins')
        return redirect(reverse,('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated')
            
        else:
            messages.error(request, 'Update failed - please check that your form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete items from the store """
    if not request.user.is_superuser:
        messages.error(request, 'That function is reserved for store admins')
        return redirect(reverse,('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('all_products'))
