from django.shortcuts import render
from django.db import models
from . models import sellGame
from .forms import SaleForm

from products.models import UserProfile


# Create your views here.

def sell(request):
    """ Renders sell page """
    model = sellGame
    form_class = SaleForm
    template_name = 'sell/sell.html'

    return render(request, 'sell/sell.html')

