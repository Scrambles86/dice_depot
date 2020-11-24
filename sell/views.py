from django.shortcuts import render
from django.views.generic.edit import FormView
from django.db import models
from .models import Game
from .forms import SaleForm
from django.contrib import messages


# Create your views here.

form = SaleForm()


def sell(request):
    """ Renders sell page """

    template = 'sell/sell.html'

    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Game details received - we will email you with an offer once we have reviewed your product')
        else : 
            messages.error(request, 'Please ensure all fields are filled out correctly')
    else:
        form = SaleForm()
        context = {
        "form": form,
    }

    return render(request, template, context)

