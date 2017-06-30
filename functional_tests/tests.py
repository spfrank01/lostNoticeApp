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


if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8