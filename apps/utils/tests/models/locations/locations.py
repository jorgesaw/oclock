"""Locations models utilities for testing."""

# Models
from apps.locations.models import (
    City,
    State
)

CITY_NAME = 'CityYÑ099.h¡8y+)¿99hsw'
STATE_NAME = 'State}{88-_.,+}{lñ'


def create_state(name=STATE_NAME, active=True):
    return State.objects.create(
        name=name,
        active=active
    )


def create_city(
    name=CITY_NAME,
    active=True,
    state=None
):

    if not state:
        state = State.objects.create(name=STATE_NAME)
    return City.objects.create(
        name=name,
        active=active,
        state=state
    )
