"""Shows forms."""

# Django
from django import forms

# Models
from apps.shows.models import Show


class ShowForm(forms.ModelForm):
    """Show form."""

    class Meta:
        model = Show
        fields = ('fantasy_name','description', 'scope_show', 'scope_radio', 'picture',
                'event', 'city'
        )
        widgets = {
            'scope_radio': forms.NumberInput( attrs={'type':'range', 'step': 10, 'min': 0, 'max':500})
        }
