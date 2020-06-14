"""Managers."""

# Django
from django.db import models


class ActiveManager(models.Manager):
    """Active manager."""
    
    def active(self):
        return self.filter(active=True)
