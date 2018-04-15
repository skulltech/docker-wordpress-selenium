import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WordpressTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)

    def test_title(self):
        self.driver.get('http://10.192.56.143:8000')
        self.assertEqual(self.driver.title, 
                            'Best WordPress Site Ever! – Just another WordPress site', 
                            'Incorrect title of homepage.')

    def tearDown(self):
        self.driver.quit()
