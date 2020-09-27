"""Core views."""

# Django
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Forms
from apps.shows.forms import ShowSearchForm

# Models
from apps.shows.models import Show


def _get_form(request, form_cls, prefix_):
    data = request.POST if prefix_ in request.POST else None
    return form_cls(data, prefix=prefix_)


class HomePageView(TemplateView, ListView):

    context_object_name = 'shows_list'
    template_name = "core/home.html"
    paginate_by = 10
    main_search_form = ShowSearchForm
   
    def get(self, request, *args, **kwargs):
        shows = Show.objects.all()
        adds_shows = Show.objects.all()

        # https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
        # https://moonbooks.org/Articles/How-to-get-visitor-ip-address-with-django-/
        # x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(',')[0]
        # else:
        #     ip = self.request.META.get('REMOTE_ADDR')

        return render(
            request,
            self.template_name,
            {
                'title': 'Inicio',
                self.context_object_name: shows,
                'adds_shows': adds_shows,
                'main_search_form': self.main_search_form(prefix='main_search_form'),
                'secondary_search_form': None
            }
        )

    def post(self, request, *args, **kwargs):
        adds_shows = Show.objects.all()
        main_search_form = _get_form(request, self.main_search_form, 'main_search_form')
        #secondary_search_form = _get_form(request, ShowSearchForm, 'secondary_search_form')
        
        if main_search_form.is_bound and main_search_form.is_valid():
            city = main_search_form.cleaned_data['city']
            event = main_search_form.cleaned_data['event']
            name = main_search_form.cleaned_data['name']

            shows = Show.objects.filter(
                city=city,
                event=event,
                name__contains=name
            )
            main_search_form = self.main_search_form(prefix='main_search_form')

        else:
            shows = Show.objects.all()

        return render(
            request,
            self.template_name,
            {
                'title': 'Inicio',
                self.context_object_name: shows,
                'adds_shows': adds_shows,
                'main_search_form': main_search_form,
                #'secondary_search_form': secondary_search_form,
            }
        )
