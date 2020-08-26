from django.shortcuts import render
from django.views.generic.edit import FormView
from django.db import models
from . models import sellGame
from .forms import SaleForm

from products.models import UserProfile


# Create your views here.

class SellFormView(FormView):
    model = sellGame
    form_class = SaleForm
    template_name = 'sell/sell.html'


def sell(request):
    """ Renders sell page """
   

    return render(request, 'sell/sell.html')

