from django.shortcuts import render
from django.views.generic.edit import FormView
from django.db import models
from .models import Game
from .forms import SaleForm


# Create your views here.

class SellFormView(FormView):
    model = Game
    form_class = SaleForm
    template_name = 'sell/sell.html'


def sell(request):
    """ Renders sell page """
    return render(request, 'sell/sell.html')

