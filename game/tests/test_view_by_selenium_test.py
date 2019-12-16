import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SeleniumTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=options)
        super(SeleniumTestCase, self).setUp()
    
    def tearDown(self):
        self.browser.close()
        super(SeleniumTestCase, self).tearDown()

    def test_find_h1_homepage(self):
        """Test to find the h1 tag in the unauthorized homepage"""
        self.browser.get(self.live_server_url + '/game/')
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('THOR', header.text)

    def test_find_h2_homepage(self):
        """Test to find the h2 tag in the unauthorized homepage"""
        self.browser.get(self.live_server_url + '/game/')
        header = self.browser.find_element_by_tag_name('h2')
        self.assertEqual('The God of Thunder', header.text)

    def test_find_img_homepage(self):
        """Test to find the img id in the unauthorized homepage"""
        self.browser.get(self.live_server_url + '/game/')
        image = self.browser.find_element_by_id('iconhome')
        print(image.get_attribute('src'))

    def test_find_img_howtopage(self):
        """Test to find the img id in the instruction page"""
        self.browser.get(self.live_server_url + '/game/howtoplay/')
        image = self.browser.find_element_by_id('iconhowto')
        print(image.get_attribute('src'))

    def test_find_h1_howtopage(self):
        """Test to find the h1 tag in the unauthorized homepage"""
        self.browser.get(self.live_server_url + '/game/howtoplay/')
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('How to play', header.text)

    def test_find_example_howtopage(self):
        """Test to find the example id in the instruction page"""
        self.browser.get(self.live_server_url + '/game/howtoplay/')
        image = self.browser.find_element_by_id('example')
        print(image.get_attribute('src'))