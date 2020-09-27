"""Images model."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from apps.shows.models import Show

# Utilities
from apps.utils.images import custom_upload_to


class Picture(models.Model):
    """Picture models.

    Representing at image by a show.
    """

    title = models.CharField(
        _('title'),
        max_length=50,
        null=True,
        blank=True
    )

    image = models.ImageField(
        _('image'),
        upload_to=custom_upload_to,
        null=True,
        blank=True,
    )

    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
