"""Socials admin."""

# Django
from django.contrib import admin

# Models
from apps.shows.models import Comment, Event, Show


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin."""

    model = Comment
    fields = ('subject', 'comment', 'rate')
    list_display = ('subject', 'comment', 'rate', 'user', 'show')
    
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
    fields = ('name', 'event')
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'event')
    #list_editable = ('username', 'social', 'order',)
    search_fields = ('name', 'event')
    list_select_related = ('event',)
    #extra = 1
