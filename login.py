from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Login:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username=username
        self.password = password

    def signin(self):
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input')))
        uid.click()
        uid.send_keys(self.username)
        paswd= self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input')
        paswd.click()
        paswd.send_keys(self.password)
        loginBTN= self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
        loginBTN.click()
        time.sleep(3)
