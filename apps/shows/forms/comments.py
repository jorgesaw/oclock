"""Comments form."""

# Django
from django import forms

# Models
from apps.shows.models import Comment


class CommentForm(forms.ModelForm):
    """Comment form."""

    class Meta:
        """Meta class."""

        model = Comment
        fields = ('subject', 'comment', 'rate')