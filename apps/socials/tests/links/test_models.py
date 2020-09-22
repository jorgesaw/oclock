"""Links models tests."""

# Django
from django.test import TestCase

# Social utils tests
from utils.tests.models.socials import create_link


class LinkModelTest(TestCase):
    """Test link model."""

    def test_repr_by_name(self):
        link = create_link()
        self.assertEqual(str(link), link.username)


if __name__ == '__main__':
    unittest.main()
