"""Event model."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utilities
from apps.utils.models import BaseModel


class Event(BaseModel):
    """Event model.

    Model that represents a event performed by a show.
    """

    name = models.CharField(
        _('event'),
        max_length=210,
        unique=True,
        error_messages={
            'unique': _('A event with that name already exists.')
        }
    )

    def __str__(self):
        """Return fantasy name."""
        return self.name
