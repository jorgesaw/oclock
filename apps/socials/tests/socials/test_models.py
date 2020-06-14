"""Socials tests."""

# Django
from django.test import TestCase

# Models
from apps.socials.models import SocialNetwork

# Socials utils test
from utils.tests.models.socials import (
    create_social,
)

SOCIAL_KEY = 'SOCIAL NETWORK -.¿+'
SOCIAL_NAME = 'Social Network A'

class SocialModelTest(TestCase):
    """Test social model."""

    def test_auto_slug_by_name_in_key_field(self):
        social = create_social(key=SOCIAL_KEY)
        self.assertEqual(social.key, f'{slugify(SOCIAL_KEY)}')

    def test_soft_delete_model_at_inactive(self):
        social = create_social()
        self.assertTrue(social.active)
        social.soft_delete()
        self.assertTrue(not social.active)

    def test_active_manager_work(self):
        create_social(**{})
        create_social(**{})
        create_social(**{'active': False})

        self.assertEqual(len(SocialNetwork.objects.active()), 2)

    def test_repr_by_name(self):
        social = create_social(name=)
        self.assertEqual(str(social), SOCIAL_NAME)


if __name__ == '__main__':
	unittest.main() 