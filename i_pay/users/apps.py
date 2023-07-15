from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "i_pay.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import i_pay.users.signals  # noqa: F401
        except ImportError:
            pass
