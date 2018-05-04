import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from accounts import ADMLOGIN, ADMPASS
from movesleeps import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def load_dumps():
    # Log in to admin panel
    driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
    driver.maximize_window()
    driver.get("http://tribe.islandsville.com/admin/index.php?r=user/auth")
    driver.implicitly_wait(4)
    email = driver.find_element_by_id('YumUserLogin_username')
    email.send_keys(ADMLOGIN)
    password = driver.find_element_by_id('YumUserLogin_password')
    password.send_keys(ADMPASS)
    log = driver.find_element_by_name('yt0')
    log.click()

    # Loading dump
    driver.get("http://tribe.islandsville.com/admin/index.php?r=users/dump")
    from_user = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[1]/td[2]/input[1]')
    from_user.click()
    from_user.send_keys('142075956295242')
    from_social_facebook = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[2]/td[1]/select/option[3]')
    from_social_facebook.click()
    button_load_dump = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[1]/td[3]/a/span')
    button_load_dump.click()
    radio_target = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[3]/td/input')
    radio_target.click()
    to_social_facebook = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[3]/td/div/select/option[3]')
    to_social_facebook.click()
    to_user = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[3]/td/div/input')
    to_user.click()
    to_user.send_keys('142075956295242')
    load_dump_button = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[4]/td[2]/a[1]/span')
    load_dump_button.click()
    time.sleep(3)
    movesleep2()
    time.sleep(1)
    okbutton = pyautogui.locateOnScreen('C:\Automation\Screens\Enixan_Admin_Panel\ok.png')
    tokbutton = pyautogui.center(okbutton)
    time.sleep(1)
    pyautogui.click(tokbutton)
    driver.close()


