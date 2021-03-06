"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # Core app
    path('', include(('apps.core.urls', 'core'), namespace='core')),

    # Auth
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include(('apps.registration.urls', 'registration'), namespace='registration')),

    # Profiles
    path('profiles/', include(('apps.profiles.urls', 'profiles'), namespace='profiles')),

    # Shows
    path('shows/', include(('apps.shows.urls', 'shows'), namespace='shows')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
