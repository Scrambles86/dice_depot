from django.shortcuts import render

# Create your views here.

def sell(request):
    """ Renders sell page """
    return render(request, 'sell/sell.html')

