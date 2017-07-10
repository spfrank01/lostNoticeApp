from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lostnotice.views import *
from lostnotice.models import LostNoticeList, FindOwnerList, userData

class HomePageTest(TestCase):

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

	def test_root_url_home(self):
		found = resolve('/') 
		self.assertEqual(found.func, home_page) 

	def test_home_use_base_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertIn(b'<title>Home</title>', response.content)
		self.assertIn(b'<div class="topnav">', response.content)
		self.assertIn(b'<div class="container">', response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))



		