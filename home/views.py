from django.shortcuts import render

# Create your views here.

def index(request):
    """ Renders index page """
    return render(request, 'home/index.html')
