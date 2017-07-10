from django.core.urlresolvers import resolve
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


class ProfileShowListTest(TestCase):

	def create_user01(self):
		userData.objects.create(
			username="user01",
			email="user01@email.com")


	def test_show_lost_notice_list(self):
		self.create_user01()
		LostNoticeList.objects.create(title="Lost_Notice_List", your_name="user01")
		response = self.client.get('/profile/%d/' % (userData.objects.first().id,))
		self.assertIn(
			'<a href="/lost_notice/1/">Lost_Notice_List</a>', 
			response.content.decode()
		)

	def test_show_find_owner_list(self):
		self.create_user01()
		FindOwnerList.objects.create(title="Find_Owner_List", your_name="user01")
		response = self.client.get('/profile/%d/' % (userData.objects.first().id,))
		self.assertIn(
			'<a href="/found_owner/1/">Find_Owner_List</a>', 
			response.content.decode()
		)


class RegisterTest(TestCase):

	def register_new(self, username):
		response = self.client.post('/register_complete/',
						data={	'username': username,
								'email' : "email@email.com",
								'password' : "password"})
		return response

	def test_register_complete(self):
		response = self.register_new("user01")
		self.assertIn('Register Complete', response.content.decode())
		#self.assertEqual(response['location'], '/')

	def test_check_to_login_buttom_of_register_complete(self):
		response = self.register_new("user01")
		self.assertIn(
			'<a href="/login_page/" id="login_page"', 
			response.content.decode()
		)
		self.assertIn('>Login</a>', response.content.decode())
		

		
	def test_register_fail(self):
		self.register_new("user01")
		response = self.register_new("user01") # register again
		self.assertIn('Register Failed', response.content.decode())

	def test_check_register_again_buttom_of_register_fail(self):
		self.register_new("user01")
		response = self.register_new("user01") # register again
		self.assertIn(
			'<a href="/register_page/" id="register_page"', 
			response.content.decode()
		)
		self.assertIn('>Register Again</a>', response.content.decode())

class LoginTest(TestCase):

	def register_user01(self):
		response = self.client.post('/register_complete/',
						data={	'username': "user01",
								'email' : "user01@email.com",
								'password' : "password"})

	def login(self, username, password):
		response = self.client.post('/login_check/',
						data={	'username': username,
								'password' : password})
		return response


	def test_login_complete(self):
		self.register_user01()
		response = self.login("user01", "password")
		self.assertEqual(response.status_code, 302)
		#self.assertIn('<title>Profile</title>', response.content.decode())

	def test_login_fail_wrong_username(self):
		self.register_user01()
		response = self.login("user00", "password")
		self.assertIn('<title>Login Fail</title>', response.content.decode())
		self.assertIn('<h1>Not User : user00</h1>', response.content.decode())

	def test_login_fail_wrong_password(self):
		self.register_user01()
		response = self.login("user01", "abc")
		self.assertIn('<title>Login Fail</title>', response.content.decode())		
		self.assertIn(
			'<h1>User : user01,  Password fail</h1>', 
			response.content.decode()
		)

	def test_show_link_off_login_fail(self):
		self.register_user01()
		response = self.login("user00", "abc")
		self.assertIn('>Login Again</a>', response.content.decode())
		self.assertIn('>Register</a>', response.content.decode())


class AddNewNoticeTest(TestCase):

	def register_user01(self):
		response = self.client.post('/register_complete/',
						data={	'username': "user01",
								'email' : "user01@email.com",
								'password' : "password"})

	def test_add_new_lost_notice(self):
		self.register_user01()
		response = self.client.post('/save_new_item_lost/',
						data={	
							'title' : "lost pen",
							'name_item' : "pen",
							'time_lost' : "now",
							'location_lost' : "unknown",
							'detail' : "unknown",
							'your_name' : "user01",
							'your_email' : "user01@email.com"
						})
		self.assertEqual("lost pen", LostNoticeList.objects.first().title)
		self.assertEqual("pen", LostNoticeList.objects.first().name_item)
		self.assertEqual("now", LostNoticeList.objects.first().time_lost)
		self.assertEqual("unknown", LostNoticeList.objects.first().location_lost)
		self.assertEqual("unknown", LostNoticeList.objects.first().detail)
		self.assertEqual("user01", LostNoticeList.objects.first().your_name)
		self.assertEqual("user01@email.com", LostNoticeList.objects.first().your_email)


	def test_add_new_find_owner(self):
		self.register_user01()
		response = self.client.post('/save_new_found_owner/',
						data={	
							'title' : "lost pen",
							'name_item' : "pen",
							'time_found' : "now",
							'location_found' : "unknown",
							'detail' : "unknown",
							'your_name' : "user01",
							'your_email' : "user01@email.com"
						})
		self.assertEqual("lost pen", FindOwnerList.objects.first().title)
		self.assertEqual("pen", FindOwnerList.objects.first().name_item)
		self.assertEqual("now", FindOwnerList.objects.first().time_found)
		self.assertEqual("unknown", FindOwnerList.objects.first().location_found)
		self.assertEqual("unknown", FindOwnerList.objects.first().detail)
		self.assertEqual("user01", FindOwnerList.objects.first().your_name)
		self.assertEqual("user01@email.com", FindOwnerList.objects.first().your_email)