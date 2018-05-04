import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts import ADMLOGIN, ADMPASS
from movesleeps import *


def detect_nation():
    # Log in to admin panel
    driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://sturm.islandsville.com/admin/index.php')
    driver.implicitly_wait(4)
    email = driver.find_element_by_id('YumUserLogin_username')
    email.send_keys(ADMLOGIN)
    password = driver.find_element_by_id('YumUserLogin_password')
    password.send_keys(ADMPASS)
    log = driver.find_element_by_name('yt0')
    log.click()

    # Choosing a test user
    fbchoose = driver.find_element_by_xpath('//*[@id="adminbar"]/table/tbody/tr/td[1]/select[2]/option[2]')
    fbchoose.click()
    fbuseres = driver.find_element_by_xpath('//*[@id="yw1"]/li[1]/a')
    fbuseres.click()
    finduser = driver.find_element_by_id('Filter__id.match')
    finduser.send_keys('185783681924469')
    missclick = driver.find_element_by_xpath('// *[ @ id = "Filter_aka.match"]')
    missclick.click()
    movesleep2()

    # Determining the nation of user
    editbutton = driver.find_element_by_xpath('//*[@id="yw0"]/table[2]/tbody/tr/td[15]/div/a[8]')
    editbutton.click()
    time.sleep(5)
    span = driver.find_element_by_xpath('//*[@id="update-form"]/table/tbody/tr[8]/td/div[1]/div[2]/div/span')
    span.click()
    global nation
    nation = span.get_attribute('storage')
    time.sleep(2)
    driver.close()



