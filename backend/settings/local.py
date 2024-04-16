"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-dqu7gk0@y)_(qib=zyzxi&aa4_y(&crmd-n&o60rtidld9@a6n')

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]