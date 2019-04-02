from django.test import TestCase, Client
from django.urls import reverse
from main.models import *
import json

class TestViews(TestCase):
	
	def setUp(self):
		self.client = Client()
		self.register_url = reverse('main:register')
#		self.login_url = reverse('login_request', args=['project1'])
		self.login_url = reverse('main:login')
		'''
		self.project1 = Post.objects.create(
				title='project1',
				body='falan filan',
				date='10-02-1989'


			)
		'''
	def test_register_GET(self):
		response = self.client.get(self.register_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/register.html')

	def test_login_GET(self):
		response = self.client.get(self.login_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/login.html')

