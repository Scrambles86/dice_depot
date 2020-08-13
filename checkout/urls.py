from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_confirm/<order_number>', views.checkout_confirm, name='checkout_confirm'),
    path('wh/', webhook, name='webhook'),

]
