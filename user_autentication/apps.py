from django.apps import AppConfig


class UserAutenticationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_autentication"

    def ready(self):
        import user_autentication.signals
