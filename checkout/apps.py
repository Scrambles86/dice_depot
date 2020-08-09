from django.apps import AppConfig


class CheckoutsConfig(AppConfig):
    name = 'checkouts'

    def ready(self):
        import checkout.signals
