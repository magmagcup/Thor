import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(exchrome_options=options)
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)
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
    
    def set_up_user(self):
        """Setup user to login"""
        self.browser.get('https://thor-thunder.herokuapp.com/game/')
        self.browser.find_element_by_class_name('btn').click()
        time.sleep(10)
        mail = self.browser.find_element_by_xpath('//*[@id="identifierId"]')
        mail.send_keys("gamethorthunder@gmail.com")
        self.browser.find_element_by_id('identifierNext').click()
        time.sleep(10)
        password = self.browser.find_element_by_xpath('//*[@name="password"]')
        password.send_keys("thorthunder1234")
        self.browser.find_element_by_id('passwordNext').click()
        time.sleep(10)

    
    def test_login_oauth(self):
        self.set_up_user()
