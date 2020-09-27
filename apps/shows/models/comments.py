"""COmment model."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from apps.shows.models import Show

# Utilities
from apps.utils.models import BaseModel


class Comment(BaseModel):
    """Comment model.

    Model that represents a comment by a show.
    """

    STATUS_DEFAULT = 'New'

    STATUS = (
        (STATUS_DEFAULT, STATUS_DEFAULT),
        ('True', 'True'),
        ('False', 'False')
    )

    comment = models.CharField(
        _('comment'),
        max_length=210,
        null=True,
        blank=True,
    )

    subject = models.CharField(
        _('subject'),
        max_length=50,
        null=True,
        blank=True,
    )

    rate = models.SmallIntegerField(
        _('rate'),
        default=1
    )

    ip = models.CharField(
        _('ip'),
        max_length=20,
        null=True,
        blank=True,
    )

    status = models.CharField(
        _('status'),
        max_length=10,
        choices=STATUS,
        default=STATUS_DEFAULT
    )

    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        """Return subject."""
        return self.subject
