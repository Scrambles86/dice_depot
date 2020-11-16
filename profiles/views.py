from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import ProfileForm

# Create your views here.

def profile(request):
    """User Profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile info updated')

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders
    }

    return render(request, template, context)

def past_orders(request, order_number):
    """
    Returns past orders for the user
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'A confirmation number for order {order_number} was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
