

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
         self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):

         self.browser.get('gttp://localhost:8000')


if __name__ == '__main__':
    unittest.main(warnings=='ignore')

