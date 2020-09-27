"""Shows views."""

# Django
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models.signals import pre_save

# Forms
from apps.shows.forms import ShowForm

# Models
from apps.shows.models import Show

# Views
from apps.utils.views.mixins import ViewBaseMixin

# Utils
from apps.utils.text import pre_save_receiver_slug_name


@method_decorator(login_required, name='dispatch')
class ShowUpdateView(SuccessMessageMixin, UpdateView):
    """Show update view."""

    form_class = ShowForm
    template_name_suffix = '_update_form'
    success_message = "Datos del show actualizados con éxito."

    def get_object(self):
        """Return show created by user."""

        show, created = Show.objects.get_or_create(user=self.request.user)
        return show

    def get_success_url(self):
        return reverse_lazy('shows:show_edit')


class ShowDetailView(ViewBaseMixin, DetailView):
    """Show detail view."""

    model = Show


pre_save.connect(pre_save_receiver_slug_name, sender=Show)
