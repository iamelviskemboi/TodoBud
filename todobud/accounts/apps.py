from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    # Registered signals
    def ready(self):
        import accounts.signals
