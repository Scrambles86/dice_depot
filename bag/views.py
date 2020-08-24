from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ Renders customers bag contents page """
    return render(request, 'bag/bag.html')

def add_item(request, item_id):
    """
    Add game to bag in chosen quantity
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

