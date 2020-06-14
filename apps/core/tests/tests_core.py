"""Core functionals tests."""

# Django
from django.shortcuts import reverse
from django.test import TestCase
from django.urls import resolve
from django.template.loader import render_to_string

from apps.core.views.core import HomePageView


class HomePageTest(TestCase):

	def setUp(self):
		self.response = self.client.get(reverse('core:home'))

	def tearDown(self):
		del self.response

	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/')
		self.assertTrue(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		self.assertTrue(self.response.status_code, 200)
	"""
	def test_view_class_exists(self):
		self.assertTrue(
			self.response.resolver_match.func.__name__, HomePageView.__name__
		)
	"""
	def test_view_uses_correct_template(self):
		self.assertTemplateUsed(self.response, 'core/home.html')

	def test_home_page_returns_correct_html(self):
		html = self.response.content.decode('utf-8')
		self.assertTrue(html.startswith('<!DOCTYPE html>\n<html lang="es">'))
		self.assertIn('<title>Inicio | Kstore</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))
	

if __name__ == '__main__':
	unittest.main() 