"""Shows forms."""

# Django
from django import forms

# Models
from apps.locations.models import City
from apps.shows.models import Event, Show


class ShowForm(forms.ModelForm):
    """Show form."""

    city = forms.ModelChoiceField(
        queryset=City.objects.filter(active=True)
    )

    class Meta:
        model = Show
        fields = ('name', 'description', 'scope_show', 'scope_radio', 'picture',
                'event', 'city'
        )
        widgets = {
            'scope_radio': forms.NumberInput(
                attrs={'type': 'range', 'step': 10, 'min': 0, 'max': 500}
            )
        }


class ShowSearchForm(forms.ModelForm):
    """Show search."""

    def __init__(self, *args, **kwargs):
        super(ShowSearchForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False

    city = forms.ModelChoiceField(
        queryset=City.objects.filter(active=True)
    )

    event = forms.ModelChoiceField(
        queryset=Event.objects.filter(active=True)
    )

    class Meta:
        model = Show
        fields = ('city', 'event', 'name')
        localized_fields = '__all__'
