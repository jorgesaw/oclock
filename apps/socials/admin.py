"""Socials admin."""

# Django
from django.contrib import admin

# Models
from apps.socials.models import SocialNetwork, UserSocialNetwork


@admin.register(UserSocialNetwork)
class UserSocialNetworkAdmin(admin.ModelAdmin):
    """User social network admin."""

    model = UserSocialNetwork
    autocomplete_fields = ('social',)
    fields = ('username', 'social', 'order')
    readonly_fields = ('created', 'modified')
    list_display = ('username', 'social', 'order')
    search_fields = ('username',)
    list_select_related = ('social',)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    """Social network admin."""

    fields = ('key', 'name', 'url', 'order','icon_class_css')
    readonly_fields = ('created', 'modified')
    list_display = ('key', 'name', 'url')
    list_editable = ('name', 'url')
    search_fields = ('name',)
