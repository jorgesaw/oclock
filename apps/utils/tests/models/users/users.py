"""Users models utilities for testing."""

# Django
from django.contrib.auth import get_user_model

PASSWORD = 'pAssw0rd!'


def create_user(username='user@example.com', password=PASSWORD, is_staff=False):
    return get_user_model().objects.create_user(
        username=username,
		email=username,  
        first_name='Test',
        last_name='User',
        password=password, 
        is_staff=is_staff
    )
