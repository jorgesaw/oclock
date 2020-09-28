"""Shows views."""

# Django
from django.http import HttpResponseRedirect
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

    def get_context_data(self, **kwargs):
        context = super(ShowDetailView, self).get_context_data(**kwargs)
        show = self.get_object()
        show.views += 1 
        show.save(update_fields=['views',])

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
    success_message = _('Comentario agregado exitosamente. Gracias por tu interés')

    def get_context_data(self, **kwargs):
        context = super(AddCommentShowView, self).get_context_data(**kwargs)
        context['a']='w'
        return context

    def post(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        form = self.form_class(request.POST)
        slug_name_show = self.kwargs['slug_name']
        show = Show.objects.get(slug_name=slug_name_show)
        #context = self.get_context_data()
        #import ipdb;ipdb.set_trace()

        #id_show = Show.objects.filter(slug_name=slug_name_show).values_list('id', flat=True)[0]
        if form.is_valid():
            comment = Comment(
                    subject=form.cleaned_data['subject'],
                    comment=form.cleaned_data['comment'],
                    rate=form.cleaned_data['rate']
            )
            comment.ip = request.META.get('REMOTE_ADDR')
           # import ipdb;ipdb.set_trace()
            comment.show = show
            comment.user = request.user

            comment.save()
            #return HttpResponseRedirect(url)

            return HttpResponseRedirect(reverse_lazy('shows:show', kwargs={'slug_name': slug_name_show}))
             
