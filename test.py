from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time


class SeleniumHelpers:
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, posy='document.body.scrollHeight', posx=0):
        self.driver.execute_script(f'window.scrollTo({posx}, {posy});')

    def wait_for_element(self, path , selector = 'CSS_SELECTOR', waiting_time=10):
        return WebDriverWait(self.driver, waiting_time).until(EC.presence_of_element_located((getattr(By, selector),path)))
