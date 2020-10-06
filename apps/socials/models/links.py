"""Users socials networks models."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from apps.socials.models.socials import SocialNetwork
from apps.utils.models import BaseModelWithoutStatus


class UserSocialNetwork(BaseModelWithoutStatus):
    """User social network class."""

    username = models.CharField(
        _('username'),
        max_length=255
    )
    social = models.ForeignKey(
        SocialNetwork,
        on_delete=models.CASCADE,
        verbose_name=_('social network')
    )
    order = models.PositiveSmallIntegerField(_('order'), default=0)

    class Meta:
        """Meta class."""

        ordering = ['order', ]
        verbose_name = _('link')
        verbose_name_plural = _('links')
        unique_together = ('social', 'username')

    def __str__(self):
        return self.username
