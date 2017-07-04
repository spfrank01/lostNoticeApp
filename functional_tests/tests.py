from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from lostnotice.models import LostNoticeList, FindOwnerList, userData
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):  #2
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

    def tearDown(self):  #3
        self.browser.quit()

    def test_check_header_bar_and_check_first_homepage(self):

        # Check Title
        self.assertIn('Home', self.browser.title)

        #Check Header Bar
        link_header_bar = self.browser.find_elements_by_tag_name('a')
        self.assertIn("Home", link_header_bar[0].text)
        self.assertIn("Login", link_header_bar[1].text)
        self.assertIn("Register", link_header_bar[2].text)
        self.assertIn("About", link_header_bar[3].text)
        print("Header bar of Homepage.. OK")
        # No more link
        #assert 4 == len(link_header_bar)
        if len(link_header_bar) > 4:
        	self.fail("Link not only Header Bar")

        # Check h1 Tag ( have 2 tags )
        h1_tag = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("lost notice List", h1_tag[0].text)
        self.assertIn("Find owner List", h1_tag[1].text)
        print("First Homepage.. OK")

    def test_register_and_login(self):
    	# register check 2 round
    	# round 1 check register complete
    	# round 2 check register fail
        for i in range(0, 0):
        	# go to register page      
            self.assertIn('Register', self.browser.title)      
            go_register = self.browser.find_elements_by_tag_name('a')[2]
            go_register.click()

            # check page
            check = self.browser.find_elements_by_tag_name('h1')
            self.assertIn("Register", check[0].text)
            print("go to register page.. OK")

            username = self.browser.find_element_by_id("id_name")
            username.send_keys("user01")

            email = self.browser.find_element_by_id("id_email")
            email.send_keys("user01@email.com")

            password = self.browser.find_element_by_id("id_password")
            password.send_keys("password")
            password.send_keys(Keys.ENTER)

            
            if i == 1:
                # check title
                self.assertIn('Register Complete', self.browser.title)
                # check h1 tag
                check = self.browser.find_elements_by_tag_name('h1')
                self.assertIn("Register Complete", check[0].text)
                # check buttom
                check_buttom_more = self.browser.find_elements_by_tag_name('a')
                self.assertIn("Login", check_buttom_more[4].text)
                print("Round 1 Regester Complete.. OK")
            else:
                # check title
                self.assertIn('Register Failed', self.browser.title)
                # check h1 tag
                check = self.browser.find_elements_by_tag_name('h1')
                self.assertIn("Register Failed", check[0].text)
                # check buttom
                check_buttom_more = self.browser.find_elements_by_tag_name('a')
                self.assertIn("Register Again", check_buttom_more[4].text)
                print("Round 2 Register Failed.. OK")
        #end register check

        # start login
        #go to login
        # Round 1 check login fail        
        go_login = self.browser.find_elements_by_tag_name('a')[1]
        go_login.click()

        # check page
        self.assertIn('Login', self.browser.title)
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Login", check[0].text)
        print("go to login page.. OK")

        username = self.browser.find_element_by_id("id_name")
        username.send_keys("user02")

        password = self.browser.find_element_by_id("id_password")
        password.send_keys("password")
        password.send_keys(Keys.ENTER)

        # check h1 tag
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Not User : user02", check[0].text)
        # check buttom
        check_buttom_more = self.browser.find_elements_by_tag_name('a')
        self.assertIn("Login Again", check_buttom_more[4].text)
        self.assertIn("Register", check_buttom_more[5].text)
        print("Round 1 Login fail.. OK")
        # end check login fail

        # start check login complete
        # go to login page
        go_login = self.browser.find_elements_by_tag_name('a')[1]
        go_login.click()

        # check page
        self.assertIn('Login', self.browser.title)
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Login", check[0].text)
        print("go to login page.. OK")

        username = self.browser.find_element_by_id("id_name")
        username.send_keys("user01")

        password = self.browser.find_element_by_id("id_password")
        password.send_keys("password")
        password.send_keys(Keys.ENTER)

        # check h1 tag
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Profile", check[0].text)
        print("Round 2 Login Complete.. OK")
        # end login check



    def test_profile_page(self):
        # add new user in data base
        saveNewUser = userData(
            username="user01", 
            email="user01@email.com", 
            password = "password",
        )
        saveNewUser.save()

        # go to profile user01
        self.browser.get(self.live_server_url+'/profile/1')

        # check header bar of profile page
        self.assertIn('Profile', self.browser.title)
        link_header_bar = self.browser.find_elements_by_tag_name('a')
        self.assertIn("Home", link_header_bar[0].text)
        self.assertIn("Profile", link_header_bar[1].text)
        self.assertIn("Add new lost notice", link_header_bar[2].text)
        self.assertIn("Add new find owner", link_header_bar[3].text)
        self.assertIn("About", link_header_bar[4].text)
        assert 5 == len(link_header_bar)
        print("Header bar of Profile page.. OK")
        
        # check detail in Profile page
        # check h1 tag
        self.assertIn("Profile", self.browser.find_elements_by_tag_name('h1')[0].text)
        # check b tag, 4 tags
        self.assertIn("user01", self.browser.find_elements_by_tag_name('b')[0].text)
        self.assertIn("user01@email.com", self.browser.find_elements_by_tag_name('b')[1].text)
        self.assertIn("lost notice list", self.browser.find_elements_by_tag_name('b')[2].text)
        self.assertIn("find owner list", self.browser.find_elements_by_tag_name('b')[3].text)
        print("Detail of Profile page.. OK")

        # check no list in profile page
        self.assertIn("no lost notice list", self.browser.page_source)
        self.assertIn("no find owner list", self.browser.page_source)
        print("no list in Profile page.. OK")







if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8