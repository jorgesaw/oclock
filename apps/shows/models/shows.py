"""Show model."""

# Django
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

# Models
from apps.shows.models import Event
from apps.locations.models import City
from apps.users.models import User

# Utilities
from apps.utils.images import custom_upload_to
from apps.utils.models import BaseModel


class Show(BaseModel):
    """Show model.

    Model that represents a show performed by a user.
    """

    SCOPE_ONLY_CITY = 'Sólo en mi localidad'
    SCOPE_ONLY_REGION = 'Sólo en mi zona'
    SCOPE_ALL_COUNTRY = 'En todo el país'

    SCOPE_SHOW_CHOICES = (
        (SCOPE_ONLY_CITY, SCOPE_ONLY_CITY),
        (SCOPE_ONLY_REGION, SCOPE_ONLY_REGION),
        (SCOPE_ALL_COUNTRY, SCOPE_ALL_COUNTRY)
    )

    fantasy_name = models.CharField(
        _('fantasy name'),
        max_length=210,
        unique=True,
        error_messages={
            'unique': _('A user with that show already exists.')
        }
    )

    description = models.TextField(max_length=3500, null=True, blank=True)

    scope_show = models.CharField(
        _('offer show'),
        max_length=25,
        choices=SCOPE_SHOW_CHOICES,
        default=SCOPE_ONLY_CITY
    )

    scope_radio = models.SmallIntegerField(_('radio'), default=0)

    picture = models.ImageField(
        'show picture',
        upload_to=custom_upload_to,
        null=True,
        blank=True
    )

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Event type')
    )

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('location')
    )

    def __str__(self):
        """Return fantasy name."""
        return self.fantasy_name


@receiver(post_save, sender=User)
def ensure_show_exists(sender, instance, **kwargs):
    """
    Señal que se encarga de crear un perfil por defecto en caso de que 
    el usuario se cree una cuenta (post_save) pero nunca ingrese a su perfil.
    """
    if kwargs.get('created', False): # Si acaba de crearse un usuario creamos el perfil
        Show.objects.get_or_create(user=instance, fantasy_name=instance.username)
        