"""Shows URLs."""

# Django
from django.urls import path
from .views import shows as shows_views

urlpatterns = [
    path('show/', shows_views.ShowUpdateView.as_view(), name='show_edit'),
    path('shows/<slug:slug_name>/', shows_views.ShowDetailView.as_view(), name='show')
]
