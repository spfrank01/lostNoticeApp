from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):  #2
        self.browser = webdriver.Firefox()

    def tearDown(self):  #3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        print(self.browser.title)
        print(self.browser.find_element_by_tag_name('h1').text)
        print(self.browser.find_element_by_tag_name('h1').text)
        self.fail('Finish the test!')  #6

        # She is invited to enter a to-do item straight away


if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8