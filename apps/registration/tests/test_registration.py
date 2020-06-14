"""Registrations users tests."""

# Django
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import TestCase

# Forms
from apps.registration.forms import UserCreationWithEmail

PASSWORD = 'pAssw0rd!'


class TestPageRegistration(TestCase):

    def test_user_signup_page_loads_correctly(self):
        response = self.client.get(reverse('registration:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertContains(response, 'Sign Up')
        self.assertIsInstance(
            response.context['form'], UserCreationWithEmail
        )

    def test_user_can_sign_up(self):
        response = self.client.post(reverse('registration:signup'), data={
            'username': 'user',
			'email': 'user@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': PASSWORD,
            'password2': PASSWORD,
        })
        self.assertEqual(302, response.status_code)
        self.assertTrue(
            get_user_model().objects.filter(
                email='user@example.com'
            ).exists()
        )
        self.assertTrue(
            not auth.get_user(self.client).is_authenticated
        )
