
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time



class MySystemTests(StaticLiveServerTestCase):
    
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        CHROMEDRIVER_PATH = '/var/www/Demo_DevOps/main/tests/chromedriver' 
        self.options.add_argument("start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.browser = webdriver.Chrome( options=self.options)        


    def tearDown(self):
        self.browser.close()

    def test_user_register_and_check_tutorials(self):
        self.browser.get(self.live_server_url)
        time.sleep(5)
 #       self.browser.close()