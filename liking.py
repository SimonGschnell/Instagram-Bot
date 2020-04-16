from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import random
from test import SeleniumHelpers


def return_random_sleep(mode='sleep'):
    return_value=0
    if mode == 'sleep':
        return_value = random.randint(2, 3)
    elif mode == 'liking':
        return_value = random.randint(13,23)
    else :
        return_value = 3
    return return_value

class Liking:
    def __init__(self, driver, hashtag):
        self.page = f'https://www.instagram.com/explore/tags/{hashtag}/'
        self.driver = driver
        self.selHelp = SeleniumHelpers(self.driver)
        self.hashtag = hashtag
        self.person_list =[]

    def get_person_list(self):
        self.driver.get(self.page)
        time.sleep(return_random_sleep())
        links = []
        hrefs = []
        for i in range(1, 8):
            self.selHelp.scroll_down()
            time.sleep(1)
            links.extend(self.driver.find_elements_by_tag_name('a'))
            currentItems = self.driver.find_elements_by_tag_name('a')
            hrefs.extend([ele.get_attribute('href') for ele in currentItems])
            time.sleep(return_random_sleep()-1)
        lischte = list(set([ ele for ele in hrefs if '/p/' in ele]))[:]
        person_lischte = lischte[-20:]
        print(len(person_lischte))
        self.person_list = person_lischte

    def like_3_posts_of_persons(self):
        print(len(self.person_list))
        for person in self.person_list:
            try:
                self.driver.get(person)
                person = self.selHelp.wait_for_element('#react-root > section > main > div > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > h2 > a')
                person.click()
                time.sleep(2)
                first_3_pics =self.driver.find_elements_by_tag_name('a')
                first_3_pics = [ele.get_attribute('href') for ele in first_3_pics]
                first_3_pics = list(set([ele for ele in first_3_pics if '/p/' in ele]))[0:3]
            except Exception as e:
                print(e)
                time.sleep(2)
                continue
            for href in first_3_pics:
                try:
                    self.driver.get(href)
                    time.sleep(1)
                    self.selHelp.scroll_down()
                    likeBtn = self.selHelp.wait_for_element('#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
                    likeBtn.click()
                    time.sleep(18)
                except Exception as a:
                    print(a)
                    time.sleep(2)






        '''for href in lischte:
            try:
                self.driver.get(href)
                time.sleep(return_random_sleep())
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                likeBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')))
                likeBtn.click()
                time.sleep(return_random_sleep('liking'))
            except Exception as a:
                print(a)
                time.sleep(return_random_sleep())
                pass'''