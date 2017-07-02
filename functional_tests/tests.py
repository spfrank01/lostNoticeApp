from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
            password.send_keys("user01")
            password.send_keys(Keys.ENTER)

            # check h1 tag
            if i == 1:
                check = self.browser.find_elements_by_tag_name('h1')
                self.assertIn("Register Complete", check[0].text)
                print("Round 1 Regester Complete.. OK")
            else:
                check = self.browser.find_elements_by_tag_name('h1')
                self.assertIn("Register Failed", check[0].text)
                print("Round 2 Register Failed.. OK")
        #end register check

        # start login
        #go to login
        # Round 1 check login fail        
        go_login = self.browser.find_elements_by_tag_name('a')[1]
        go_login.click()

        # check page
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Login", check[0].text)
        print("go to login page.. OK")

        username = self.browser.find_element_by_id("id_name")
        username.send_keys("user02")

        password = self.browser.find_element_by_id("id_password")
        password.send_keys("user02")
        password.send_keys(Keys.ENTER)

        # check h1 tag
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Not User : user02", check[0].text)
        print("Round 1 Login fail.. OK")
        # end check login fail

        # start check login complete
        # go to login page
        go_login = self.browser.find_elements_by_tag_name('a')[1]
        go_login.click()

        # check page
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Login", check[0].text)
        print("go to login page.. OK")

        username = self.browser.find_element_by_id("id_name")
        username.send_keys("user01")

        password = self.browser.find_element_by_id("id_password")
        password.send_keys("user01")
        password.send_keys(Keys.ENTER)

        # check h1 tag
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Profile", check[0].text)
        print("Round 2 Login Complete.. OK")
        # end login check



        





if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8