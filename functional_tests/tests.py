from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from lostnotice.models import LostNoticeList, FindOwnerList, userData

import time
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
        # No more link
        #assert 4 == len(link_header_bar)
        if len(link_header_bar) > 4:
        	self.fail("Link not only Header Bar")

        # Check h1 Tag ( have 2 tags )
        h1_tag = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("lost notice List", h1_tag[0].text)
        self.assertIn("Find owner List", h1_tag[1].text)


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
            else:
                # check title
                self.assertIn('Register Failed', self.browser.title)
                # check h1 tag
                check = self.browser.find_elements_by_tag_name('h1')
                self.assertIn("Register Failed", check[0].text)
                # check buttom
                check_buttom_more = self.browser.find_elements_by_tag_name('a')
                self.assertIn("Register Again", check_buttom_more[4].text)
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
        # end check login fail

        # start check login complete
        # go to login page
        go_login = self.browser.find_elements_by_tag_name('a')[1]
        go_login.click()

        # check page
        self.assertIn('Login', self.browser.title)
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Login", check[0].text)

        username = self.browser.find_element_by_id("id_name")
        username.send_keys("user01")

        password = self.browser.find_element_by_id("id_password")
        password.send_keys("password")
        password.send_keys(Keys.ENTER)

        # check h1 tag
        check = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Profile", check[0].text)
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
        time.sleep(0.2)
        #assert 5 == len(link_header_bar)
        
        # check detail in Profile page
        # check h1 tag
        self.assertIn("Profile", self.browser.find_elements_by_tag_name('h1')[0].text)
        # check b tag, 4 tags
        self.assertIn("user01", self.browser.find_elements_by_tag_name('b')[0].text)
        self.assertIn("user01@email.com", self.browser.find_elements_by_tag_name('b')[1].text)
        self.assertIn("lost notice list", self.browser.find_elements_by_tag_name('b')[2].text)
        self.assertIn("find owner list", self.browser.find_elements_by_tag_name('b')[3].text)

        # check no list in profile page
        self.assertIn("no lost notice list", self.browser.page_source)
        self.assertIn("no find owner list", self.browser.page_source)



    def test_add_new_lost_notice(self):
        time.sleep(0.2)
        # add new user in data base
        saveNewUser = userData(
            username="user01", 
            email="user01@email.com", 
            password = "password",
        )
        saveNewUser.save()
        time.sleep(0.2)

        # go to add lost notice page
        self.browser.get(self.live_server_url+'/1/add_new_lost_notice/')

        # check Add Lost Notice page
        self.assertIn('Add Lose Notice', self.browser.title)
        h1_tag = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Add Lose Notice", h1_tag[0].text)
        
        # input data
        title = self.browser.find_element_by_id("id_title")
        title.send_keys("Lost No.01")

        name_item = self.browser.find_element_by_id("id_name_item")
        name_item.send_keys("Item No.01")
        
        detail = self.browser.find_element_by_id("id_detail")
        detail.send_keys("detail")
        
        time_lost = self.browser.find_element_by_id("id_time_lost")
        time_lost.send_keys("time now")
        
        location_lost = self.browser.find_element_by_id("id_location_lost")
        location_lost.send_keys("this")
        # click Enter (submit)
        location_lost.send_keys(Keys.ENTER)
        time.sleep(0.2)

        #check link new lost notice in profile page (Lost No.01)
        assert 6 == len(self.browser.find_elements_by_tag_name('a'))
        self.assertIn('Profile', self.browser.title)
        self.assertIn("Lost No.01" ,self.browser.find_elements_by_tag_name('a')[5].text)     

        # go to Homepage     
        self.browser.find_elements_by_tag_name('a')[0].click()
        self.assertIn('Home', self.browser.title)

        #check link new lost notice in Homepage (Lost No.01)
        self.assertIn("Lost No.01" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("no find owner list", self.browser.page_source)

        # go to Lost No.01 page
        self.browser.find_elements_by_tag_name('a')[4].click()

        # check Lost No.01 page             
        self.assertIn('Detail Lost Notice', self.browser.title)
        self.assertIn ("Detail Lost Notice", self.browser.find_elements_by_tag_name('h2')[0].text)
        self.assertIn ("Lost No.01", self.browser.find_elements_by_tag_name('h1')[0].text)

        # check detail in page source
        self.assertIn("Name item : Item No.01", self.browser.page_source)
        self.assertIn("Detail : detail", self.browser.page_source)
        self.assertIn("Time lost : time now", self.browser.page_source)
        self.assertIn("Location : this", self.browser.page_source)
        self.assertIn("Found It : False", self.browser.page_source)
        self.assertIn("Username : user01", self.browser.page_source)
        self.assertIn("Email : user01@email.com", self.browser.page_source)


    def test_add_new_find_owner(self):
        # add new user in data base
        saveNewUser = userData(
            username="user01", 
            email="user01@email.com", 
            password = "password",
        )
        saveNewUser.save()
        self.browser.get(self.live_server_url+'/profile/1')
        time.sleep(0.2)

        # go to add find owner page
        self.browser.get(self.live_server_url+'/1/add_new_found_owner/')

        # check Add Find Owner page
        self.assertIn('Add New Find Owner', self.browser.title)
        h1_tag = self.browser.find_elements_by_tag_name('h1')
        self.assertIn("Add New Find Owner", h1_tag[0].text)
        
        # input data
        title = self.browser.find_element_by_id("id_title")
        title.send_keys("Find No.01")

        name_item = self.browser.find_element_by_id("id_name_item")
        name_item.send_keys("Item No.01")
        
        detail = self.browser.find_element_by_id("id_detail")
        detail.send_keys("detail")
        
        time_lost = self.browser.find_element_by_id("id_time_lost")
        time_lost.send_keys("time now")
        
        location_lost = self.browser.find_element_by_id("id_location_lost")
        location_lost.send_keys("this")
        # click Enter (submit)
        location_lost.send_keys(Keys.ENTER)
        time.sleep(0.2)

        #check link new lost notice in profile page (Lost No.01)
        assert 6 == len(self.browser.find_elements_by_tag_name('a'))
        self.assertIn('Profile', self.browser.title)
        self.assertIn("Find No.01" ,self.browser.find_elements_by_tag_name('a')[5].text)    

        # go to Homepage     
        self.browser.find_elements_by_tag_name('a')[0].click()
        self.assertIn('Home', self.browser.title)

        #check link new lost notice in Homepage (Lost No.01)
        self.assertIn("Find No.01" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("no lost notice list", self.browser.page_source)       

        # go to Find No.01 page
        self.browser.find_elements_by_tag_name('a')[4].click()

        # check Find No.01 page             
        self.assertIn('Detail Find Owner', self.browser.title)
        self.assertIn ("Detail Find Owner", self.browser.find_elements_by_tag_name('h2')[0].text)
        self.assertIn ("Find No.01", self.browser.find_elements_by_tag_name('h1')[0].text)

        # check detail in page source
        self.assertIn("Name item : Item No.01", self.browser.page_source)
        self.assertIn("Detail : detail", self.browser.page_source)
        self.assertIn("Time lost : time now", self.browser.page_source)
        self.assertIn("Location : this", self.browser.page_source)
        self.assertIn("Find status : False", self.browser.page_source)
        self.assertIn("Username : user01", self.browser.page_source)
        self.assertIn("Email : user01@email.com", self.browser.page_source)

     # use lost notice
     # set N = 2 (max list in 1 page)
     # add 5 list, show 3 pages
    def test_limit_list(self):
        # add new user in data base
        saveNewUser = userData(
            username="user01", 
            email="user01@email.com", 
            password = "password",
        )
        saveNewUser.save()

        # add First list 
        self.add_new_lost_notice('First list')
        time.sleep(0.2)
        self.assertIn("First list" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("now Page 1", self.browser.page_source)
        # A Tag, header bar 4 tags + lost list 1 tag
        assert 5 == len(self.browser.find_elements_by_tag_name('a'))

        # add Second list 
        self.add_new_lost_notice('Second list')
        time.sleep(0.2)
        self.assertIn("Second list" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("First list" ,self.browser.find_elements_by_tag_name('a')[5].text)
        self.assertIn("now Page 1", self.browser.page_source)
        # A Tag, header bar 4 tags + lost list 2 tags
        assert 6 == len(self.browser.find_elements_by_tag_name('a'))

        # add Third list 
        self.add_new_lost_notice('Third list')
        time.sleep(0.2)
        self.assertIn("Third list" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("Second list" ,self.browser.find_elements_by_tag_name('a')[5].text)
        self.assertNotIn("First list", self.browser.page_source)
        self.assertIn("now Page 1", self.browser.page_source)
        # A Tag, header bar 4 tags + lost list 2 tags + link to_2 1 tag
        assert 7 == len(self.browser.find_elements_by_tag_name('a'))

        self.browser.find_element_by_link_text('to 2').click()
        self.assertIn("First list" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("now Page 2", self.browser.page_source)
        # A Tag, header bar 4 tags + lost list 1 tag + link to_1 1 tag
        assert 6 == len(self.browser.find_elements_by_tag_name('a'))

        # add Fourth and Fifth list 
        self.add_new_lost_notice('Fourth list')
        time.sleep(0.2)
        self.add_new_lost_notice('Fifth list')
        time.sleep(0.2)
        self.assertIn("Fifth list" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("Fourth list" ,self.browser.find_elements_by_tag_name('a')[5].text)
        self.assertIn("now Page 1", self.browser.page_source)
        # A Tag, header bar 4 tags + lost list 2 tags + link to_2 1 tag
        assert 7 == len(self.browser.find_elements_by_tag_name('a'))


        # switch page, Now page1, start to 2 > 3 > 2 >1
        self.browser.find_element_by_link_text('to 2').click()
        self.assertIn("Third list" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("Second list" ,self.browser.find_elements_by_tag_name('a')[5].text)
        self.assertIn("now Page 2", self.browser.page_source)
        # A Tag, header bar 4 tags + lost list 2 tags 
        #        + link to_1 1 tag + link to_3 1 tag
        assert 8 == len(self.browser.find_elements_by_tag_name('a'))

        # Go to page 3
        self.browser.find_element_by_link_text('to 3').click()
        self.assertIn("First list" ,self.browser.find_elements_by_tag_name('a')[4].text)
        self.assertIn("now Page 3", self.browser.page_source)
        # A Tag, header bar 4 tags + lost list 1 tag + link to_2 1 tag
        assert 6 == len(self.browser.find_elements_by_tag_name('a'))

        # Go to page 2
        time.sleep(1)
        self.browser.find_element_by_link_text('to 2').click()
        self.assertIn("now Page 2", self.browser.page_source)

        # Go to page 1
        time.sleep(1)
        self.browser.find_element_by_link_text('to 1').click()
        self.assertIn("now Page 1", self.browser.page_source)

        
    
    def add_new_lost_notice(self, title_name):
    	# go to add lost notice page
        self.browser.get(self.live_server_url+'/1/add_new_lost_notice/')
        
        # input data
        title = self.browser.find_element_by_id("id_title")
        title.send_keys(title_name)

        name_item = self.browser.find_element_by_id("id_name_item")
        name_item.send_keys("Item No.01")
        
        detail = self.browser.find_element_by_id("id_detail")
        detail.send_keys("detail")
        
        time_lost = self.browser.find_element_by_id("id_time_lost")
        time_lost.send_keys("time now")
        
        location_lost = self.browser.find_element_by_id("id_location_lost")
        location_lost.send_keys("this")
        # click Enter (submit)
        location_lost.send_keys(Keys.ENTER)
        time.sleep(0.2)    

        # go to Homepage     
        self.browser.find_elements_by_tag_name('a')[0].click()
        self.assertIn('Home', self.browser.title)

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8