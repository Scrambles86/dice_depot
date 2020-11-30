from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import ProfileForm

from checkout.models import Order

# Create your views here.

@login_required
def profile(request):
    """User Profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile info updated')
        else:
            messages.error(request, 'Something went wrong - please ensure all fields are valid')
    else:
        form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    print(orders)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

def past_orders(request, order_number):
    """
    Returns past orders for the user
    """
    orders = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'A confirmation number for order {order_number} was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': orders,
        'from_profile': True,
    }


    return render(request, template, context)
