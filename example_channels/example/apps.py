from django.apps import AppConfig

class ExampleConfig(AppConfig):
    name = 'example'

    def ready(self):
        from .signals import user_logged_in, user_logged_out
