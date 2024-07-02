from django.apps import AppConfig


class AccountConfig(AppConfig):
    label = 'account'
    name = 'infrastructure.db.account'
    verbose_name = 'Account'

    def ready(self):
        from . import signals