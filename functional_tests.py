from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user checks out the homepage of a to-do app
        self.browser.get('http://localhost:8000')
        # Notices title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User adds a couple of to-do items to the lists
        # and notices the url changed, after visiting the same
        # url user realizes its the same list
if __name__ == '__main__':
    unittest.main(warnings='ignore')
