from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile


class StripeWebhook:

    def __init__(self, request):
        self.request = request

    def confirm_order(self, order):
        """
        Sends out confirmation email on completion of order
        """
        confirm_email = order.email
        subject = render_to_string(
            'checkout/checkout_emails/subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/checkout_emails/body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL
            [cust_email]
        )

    def event_error(self, event):

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def event_payment_success(self, event):

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def event_payment_failure(self, event):

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)