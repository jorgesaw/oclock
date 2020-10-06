"""Comments form."""

# Django
from django import forms

# Models
from apps.shows.models import Comment


class CommentShowForm(forms.ModelForm):
    """Comment show form."""

    class Meta:
        """Meta class."""

        model = Comment
        fields = ('comment', 'rate')
