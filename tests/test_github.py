import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class GithubTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)

    def test_title(self):
        self.driver.get('https://github.com')
        self.assertEqual(self.driver.title, 
                            "The world's leading software development platform · GitHub", 
                            'Incorrect title of homepage.')

    def tearDown(self):
        self.driver.quit()
