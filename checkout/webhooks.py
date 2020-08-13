from django.http import HttpResponse


class StripeWebhook:

    def __init__(self, request):
        self.request = request

    def event_error(self, event):

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)