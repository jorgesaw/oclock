"""Links models tests."""

# Django
from django.test import TestCase

# Social utils tests
from utils.tests.models.socials import create_link

LINK_USERNAME = 'username0{ñl8'


class LinkModelTest(TestCase):
    """Test link model."""

    def test_repr_by_name(self):
        link = create_link()
        self.assertEqual(str(link), link.username)


if __name__ == '__main__':
    unittest.main()
