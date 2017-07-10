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


class ShowListInHomepageTest(TestCase):
	# LFList = LostFindList
	# baseUrl/lostNoticeListPage/findOwnerListPage
	# Ex. self.client.get('/2/1') = baseUrl/2/1
	#	page of lost notice list = 2
	#	page of finw owner list  = 1

	def test_show_lost_notice_list(self):
		LostNoticeList.objects.create(title="First_List")
		response = self.client.get('/')
		self.assertIn(
			'<a href="/lost_notice/1/" class="btn btn-link">First_List</a>', 
			response.content.decode()
		)
		self.assertNotIn('<a href="/lost_notice/2/"', response.content.decode())

	def test_show_link_next_to_page_2_of_lost_notice_list(self):
		LostNoticeList.objects.create(title="First_List")
		LostNoticeList.objects.create(title="Second_List")
		LostNoticeList.objects.create(title="Third_List")
		response = self.client.get('/')
		self.assertIn('<a href="/LFList/2/1/"', response.content.decode())
		self.assertNotIn('<a href="/LFList/1/2/"', response.content.decode())

	def test_show_link_back_to_page_1_of_lost_notice_list(self):
		LostNoticeList.objects.create(title="First_List")
		LostNoticeList.objects.create(title="Second_List")
		LostNoticeList.objects.create(title="Third_List")
		response = self.client.get('/LFList/2/1/')
		self.assertIn('<a href="/LFList/1/1/"', response.content.decode())


	def test_show_find_owner_list(self):
		FindOwnerList.objects.create(title="First_List")
		response = self.client.get('/')
		self.assertIn(
			'<a href="/found_owner/1/" class="btn btn-link">First_List</a>', 
			response.content.decode()
		)
		self.assertNotIn('<a href="/found_owner/2/"', response.content.decode())

	def test_show_link_next_to_page_2_of_find_owner_list(self):
		FindOwnerList.objects.create(title="First_List")
		FindOwnerList.objects.create(title="Second_List")
		FindOwnerList.objects.create(title="Third_List")
		response = self.client.get('/')
		self.assertIn('<a href="/LFList/1/2/"', response.content.decode())
		self.assertNotIn('<a href="/LFList/2/1/"', response.content.decode())

	def test_show_link_back_to_page_1_of_find_owner_list(self):
		FindOwnerList.objects.create(title="First_List")
		FindOwnerList.objects.create(title="Second_List")
		FindOwnerList.objects.create(title="Third_List")
		response = self.client.get('/LFList/1/2/')
		self.assertIn('<a href="/LFList/1/1/"', response.content.decode())




		