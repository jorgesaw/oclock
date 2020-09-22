"""Shows URLs."""

# Django
from django.urls import path
from .views import shows as shows_views

urlpatterns = [
    path('show/', shows_views.ShowUpdateView.as_view(), name='show_edit')
]
