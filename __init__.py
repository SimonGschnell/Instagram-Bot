from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
from login import Login
from getpages import Getpages
from liking import Liking

username = 'secret'
password = 'secret'
driver = 0

def main():
    global driver
    driver = webdriver.Chrome('C://Users/icecu/Desktop/instagram_driver/chromedriver.exe')
    l = Login(driver, username, password)
    l.signin()
    like = Liking(driver, 'like4like')
    like.get_person_list()
    like.like_3_posts_of_persons()
    #gp = Getpages(driver)


if __name__ == '__main__':
    main()
