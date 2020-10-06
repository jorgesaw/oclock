"""User social networf forms."""

# Django
from django import forms
from django.forms import BaseInlineFormSet
from django.forms.models import inlineformset_factory

# Models
from apps.socials.models import UserSocialNetwork
from apps.shows.models import Show


class BaseUserSocialNetworkInlineFormSet(BaseInlineFormSet):
    """Base user social network inline form set."""

    def clean(self):
        super(BaseUserSocialNetworkInlineFormSet, self).clean()
        if any(self.errors):
            return
        for form in self.forms:
            if form.cleaned_data:
                username = form.cleaned_data['username']
                social = form.cleaned_data['social']

                if not username:
                    raise forms.ValidationError(
                        'Es obligatorio un nombre de usuario.',
                        code='without_username'
                    )
                if not social:
                    raise forms.ValidationError(
                        'Es obligatorio seleccionar la red social.',
                        code='without_social_network'
                    )


class UserSocialNetworkInlineForm(forms.ModelForm):
    """User social network inline form."""

    class Meta:
        """Meta class."""

        model = UserSocialNetwork
        exclude = ('created', 'modified')


UserSocialNetworkInlineFormSet = inlineformset_factory(
    Show,
    UserSocialNetwork,
    form=UserSocialNetworkInlineForm,
    formset=BaseUserSocialNetworkInlineFormSet,
    fields=['social', 'username'],
    extra=1,
    can_delete=True
)
