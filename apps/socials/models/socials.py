"""Socials moddels."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Managers
from apps.utils.models.managers import ActiveManager

# Models
from apps.utils.models import BaseModel


class SocialNetwork(BaseModel):
    """Social network class."""

    key = models.SlugField(_('key name'), max_length=100, unique=True)
    name = models.CharField(_('social network'), max_length=255, unique=True)
    url = models.URLField(
        _('link'),
        max_length=255,
        null=True,
        blank=True
    )
    icon_class_css = models.CharField(
        _('icon of css class'),
        max_length=255,
        null=True,
        blank=True
    )

    objects = ActiveManager()

    class Meta:
        """Meta class."""

        ordering = ['name', ]
        verbose_name = _('social network')
        verbose_name_plural = _('socials networks')

    def __str__(self):
        return self.name
