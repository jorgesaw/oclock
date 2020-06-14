"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lzy as _

# Utilities
from apps.utils.models import BaseModel


class User(BaseModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extre fields.
    """

    email = models.EmailField(
        _('email address'), 
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists.')
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message=_('Phone numbermust be entered in the format: +99999999. Up to 15 digits allowed.')
    )
    phone_number = models.CharField(
        validators=[phone_regex, ],
        max_length=17,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    is_client = models.BooleanField(
        _('client'),
        default=True,
        help_text=(
            _('Help easily distinguish users and perform queries. '
            'Clientes are the main type of user')
        )
    )

    is_consumer = models.BooleanField(
        _('consumer'),
        default=False,
        help_text=(
            _('Help easily distinguish users client and consumer and perform queries.')
        )
    )

    is_verified = models. BooleanField(
        _('verified'),
        default=False,
        help_text=_('Set to true when the user have verified its email address.')
    )

    def __str__(self):
        """Return email."""
        return self.email

    def get_short_name(self):
        """Return username."""
        return self.username
