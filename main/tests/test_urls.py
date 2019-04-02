from django.test import SimpleTestCase
from django.urls import reverse,  resolve
from main.views import *

class TestUrls(SimpleTestCase):

	def test_list_url_is_reserved_register(self):
		url = reverse('main:register')
		self.assertEqual(url, '/register/')
	
	def test_list_is_resolved_register(self):
		resolver = resolve('/register/')
		self.assertEqual(resolver.view_name, 'main:register')

	def test_list_url_is_reserved_login(self):
		url = reverse('main:login')
		self.assertEqual(url, '/login/')
	
	def test_list_is_resolved_login(self):
		resolver = resolve('/login/')
		self.assertEqual(resolver.view_name, 'main:login')

	def test_list_url_is_reserved_logout(self):
		url = reverse('main:logout')
		self.assertEqual(url, '/logout/')
	
	def test_list_is_resolved_logout(self):
		resolver = resolve('/logout/')
		self.assertEqual(resolver.view_name, 'main:logout')

