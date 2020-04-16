from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time


class Getpages:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.instagram.com/the_patrick_gschnell/')
        self.flw_number = self.get_num_flw()
        print(self.flw_number)
        # 12 profiles get loaded after each scrolldown

    def get_num_flw(self):
        flw_num = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')))
        number =flw_num.get_attribute("title").replace(',','')

        return int(number)

    def get_followers(self):
        followerBtn=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')))
        followerBtn.click()
        popUp = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]')))
        self.sriver.execute_script('argument[0].scrollTop = arguments[0].scrollHeight', popUp)