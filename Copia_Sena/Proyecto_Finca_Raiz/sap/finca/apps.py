from django.apps import AppConfig


class FincaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finca'

class AccountsConfig(AppConfig):
    name = 'accounts'
