from django.shortcuts import render
from django.views.generic.edit import FormView
from django.db import models
from .models import Game
from .forms import SaleForm


# Create your views here.

form = SaleForm()

def sell(request):
    """ Renders sell page """

    template =  'sell/sell.html'
    context = {
        "form": form 
    }

    return render(request, template, context)

