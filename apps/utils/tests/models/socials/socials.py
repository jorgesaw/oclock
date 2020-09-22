"""Socials models utilities for testing."""

from apps.socials.models import (
    Link,
    SocialNetwork
)

LINK_USERNAME = 'username0{ñl8'
SOCIAL_KEY_NAME = 'RED SOCIAL oio'
SOCIAL_NAME = 'Red social oiouo'


def create_social(
    name=SOCIAL_NAME,
    key=SOCIAL_KEY_NAME,
    active=True
):
    return SocialNetwork.objects.create(
        name=name,
        key=key,
        active=active
    )


def create_link(
    username=LINK_USERNAME,
    social=None
):

    if not social:
        social = SocialNetwork.objects.create(
            name='SOCIAL G',
            key='SOCIAL_KEY_NAME',
        )
    return Link.objects.create(
        username=username,
        social=social
    )
