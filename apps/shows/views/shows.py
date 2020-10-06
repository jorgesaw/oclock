"""Shows views."""

# Python
import decimal

# Django
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import transaction
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

# Forms
from apps.shows.forms import (
        ShowForm,
        CommentShowForm
)
from apps.socials.forms import UserSocialNetworkInlineFormSet

# Models
from apps.shows.models import (
        Show,
        Comment
)

# Views
from apps.utils.views.mixins import ViewBaseMixin

# Utils
from apps.utils.text import pre_save_receiver_slug_name


@method_decorator(login_required, name='dispatch')
class ShowUpdateView(SuccessMessageMixin, UpdateView):
    """Show update view."""

    model = Show
    form_class = ShowForm
    template_name_suffix = '_update_form'
    success_message = "Datos del show actualizados con éxito."

    def get_context_data(self, **kwargs):
        context = super(ShowUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['items_socials'] = UserSocialNetworkInlineFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context['items_socials'] = UserSocialNetworkInlineFormSet(
                    instance=self.object
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        items_socials = context['items_socials']
        with transaction.atomic():
            self.object = form.save()
            if items_socials.is_valid():
                items_socials.instance = self.object
                items_socials.save()
        return super(ShowUpdateView, self).form_valid(form)

    def get_object(self):
        """Return show created by user."""

        show, created = Show.objects.get_or_create(user=self.request.user)
        return show

    def get_success_url(self):
        return reverse_lazy('shows:show_edit')


class ShowDetailView(ViewBaseMixin, DetailView):
    """Show detail view."""

    model = Show

    def get_context_data(self, **kwargs):
        context = super(ShowDetailView, self).get_context_data(**kwargs)
        show = self.get_object()
        show.views += 1 
        show.save(update_fields=['views', ])
        comments = Comment.objects.filter(show=show)
        context['comments'] = comments
        return context


pre_save.connect(pre_save_receiver_slug_name, sender=Show)


class AddCommentShowView(SuccessMessageMixin, CreateView):
    """Add comment show view."""

    model = Comment
    form_class = CommentShowForm
    slug_field = 'slug_name'
    slug_url_kwarg = 'slug_name'
    success_message = _(
            'Comentario agregado exitosamente. Gracias por tu interés'
    )

    def get_context_data(self, **kwargs):
        context = super(AddCommentShowView, self).get_context_data(**kwargs)
        context['a'] = 'w'
        return context

    def post(self, request, *args, **kwargs):
        #url = request.META.get('HTTP_REFERER')
        form = self.form_class(request.POST)
        slug_name_show = self.kwargs['slug_name']
        show = Show.objects.get(slug_name=slug_name_show)

        if form.is_valid():
            comment = Comment(
                    comment=form.cleaned_data['comment'],
                    rate=form.cleaned_data['rate']
            )
            comment.ip = request.META.get('REMOTE_ADDR')
            comment.show = show
            comment.user = request.user

            comment.save()
            if not show.rate:  # First ranking
                show.rate = comment.rate
            new_rate_show = (decimal.Decimal(show.rate) + comment.rate) / 2
            new_rate_show = decimal.Decimal(new_rate_show).quantize(
                    decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP
            )
            show.rate = new_rate_show
            show.save(update_fields=['rate', ])

            #return HttpResponseRedirect(url)
            messages.success(request, self.success_message)
        return HttpResponseRedirect(
                reverse_lazy(
                    'shows:show', kwargs={'slug_name': slug_name_show}
                )
        )
