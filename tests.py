from django.test import TestCase
from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        coloncare=driver.find_element(By.CSS_SELECTOR,'.header-login')
        coloncare.click()
        time.sleep(2)
        coloncare=driver.find_element(By.CSS_SELECTOR,'.floating')
        coloncare.send_keys("admin")
        time.sleep(2)
        coloncare=driver.find_element(By.ID,'passwordlog')
        coloncare.send_keys("admin")
        time.sleep(2)
        
        coloncare=driver.find_element(By.CSS_SELECTOR,'#submit')
        coloncare.click()
        time.sleep(2)
        coloncare=driver.find_element(By.ID,'user')
        coloncare.click()
        time.sleep(2)
      
        coloncare=driver.find_element(By.ID,'role')
        coloncare.click()
        time.sleep(2)
        coloncare=driver.find_element(By.ID,'doctor')
        coloncare.click()
        time.sleep(2)
        print("Filtered Doctors")
        # time.sleep(2)
        # coloncare=driver.find_element(By.ID,'basedoctor')
        # coloncare.click()
        # time.sleep(2)
        

# Create your tests here.
