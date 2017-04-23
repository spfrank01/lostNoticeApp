from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser.implicitly_wait(3)

    def tearDown(self):  #3
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Lose Noitce', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Lose Noitce', header_text)

        #add_new_item_lost()
        self.assertTrue(self.browser.find_element_by_id('add_new_lost_item'))
        self.assertIn('NEW', self.browser.find_element_by_id('add_new_lost_item').text)
        #print(self.browser.find_element_by_tag_name('a').text)
        self.assertEqual(self.browser.find_element_by_id('add_new_lost_item'), self.browser.find_element_by_tag_name('a'))







        #self.browser.get('http://localhost:8000/add_new_lost_item')
        link = self.browser.find_element_by_link_text('NEW')
        link.click()
        #self.browser.refresh()
        self.browser.get('http://localhost:8000/add_new_lost_item')
        #Name Item Lost
        inputbox = self.browser.find_element_by_id('id_name_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter name item'
        )
        inputbox.send_keys('Pen')
        
        #Detail Item Lost
        inputbox = self.browser.find_element_by_id('id_detail')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter Detail item lost'
        )
        inputbox.send_keys('at KMUTNB')
        
        #Your name Item Lost
        inputbox = self.browser.find_element_by_id('id_your_name')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter Your name'
        )
        inputbox.send_keys('Peter')
        
        #Your e-mail
        inputbox = self.browser.find_element_by_id('id_your_email')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your e-mail'
        )
        inputbox.send_keys('abc@email.com')

        inputbox.send_keys(Keys.ENTER)


        self.browser.get('http://localhost:8000')
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('td')
        #self.assertIn('Pen', [row.text for row in rows])
        link = self.browser.find_element_by_link_text('Pen')
        link.click()

        self.browser.get('http://localhost:8000/1')
        div_text = self.browser.find_element_by_tag_name('div')
        #assertIn('Pen', [row.text for row in div_text] )
        self.assertIn('Detail Lost Noitce', self.browser.find_element_by_tag_name('h1').text)
        self.assertIn('Pen', self.browser.find_element_by_tag_name('h2').text)
        self.assertTrue(self.browser.find_element_by_tag_name('div'))
        self.assertIn('at KMUTNB', self.browser.find_element_by_id('detail').text)
        self.assertIn('Peter', self.browser.find_element_by_id('your_name').text)
        self.assertIn('abc@email.com', self.browser.find_element_by_id('your_email').text)

if __name__ == '__main__':
	unittest.main(warnings='ignore')