"""Shows views."""

# Django
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Forms
from apps.shows.forms import ShowForm

# Models
from apps.shows.models import Show


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