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
        self.browser = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.wait = WebDriverWait(self.browser, 10)
        super(SeleniumTestCase, self).setUp()
    
    def tearDown(self):
        self.browser.close()
        super(SeleniumTestCase, self).tearDown()
    
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