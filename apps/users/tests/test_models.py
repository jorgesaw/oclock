"""Models users tests."""

# Django
from django.test import TestCase

# Models
from apps.users.models import User

# User create
from apps.utils.tests.models import create_user, PASSWORD


class UserModelTest(TestCase):

    def setUp(self):
        self.test_user = User(email='user@test.com', password=PASSWORD)
        self.test_user.save()

    def test_user_to_string_email(self):
        self.assertEquals(str(self.test_user), 'user@test.com')

    def tearDown(self):
        self.test_user.delete()

