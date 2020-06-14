"""Socials admin."""

# Django
from django.contrib import admin

# Models
from apps.socials.models import Link, SocialNetwork


class LinkAdmin(admin.TabularInline):
    """Link admin."""

    model = Link
    autocomplete_fields = ('social',)
    fields = ('username', 'social', 'order')
    readonly_fields = ('created', 'modified')
    list_display = ('username', 'social', 'order')
    list_editable = ('username', 'social', 'order',)
    search_fields = ('username',)
    list_select_related = ('social',)
    extra = 1


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    """Social network admin."""

    fields = ('key', 'name', 'url', 'icon_class_css')
    readonly_fields = ('created', 'modified')
    list_display = ('key', 'name', 'url')
    list_editable = ('key', 'name', 'url')
    search_fields = ('name',)
