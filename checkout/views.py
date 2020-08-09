from django.shortcuts import render


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error.request, "Your bag is empty"
        return redirect(reverse('products'))
