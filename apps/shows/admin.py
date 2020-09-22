"""Socials admin."""

# Django
from django.contrib import admin

# Models
from apps.shows.models import Event, Show


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Event admin."""

    model = Event
    fields = ('name',)
    readonly_fields = ('created', 'modified')
    list_display = ('name',)
    # list_editable = ('name',)
    search_fields = ('name',)


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    """Show admin."""

    model = Show
    autocomplete_fields = ('city',)
    fields = ('fantasy_name', 'event')
    readonly_fields = ('created', 'modified')
    list_display = ('fantasy_name', 'event')
    #list_editable = ('username', 'social', 'order',)
    search_fields = ('fantasy_name', 'event')
    list_select_related = ('event',)
    #extra = 1
