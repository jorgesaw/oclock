"""Socials app"""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SocialsAppConfig(AppConfig):
    """Socials app config."""

    name = 'apps.socials'
    verbose_name = _('socials networks')
