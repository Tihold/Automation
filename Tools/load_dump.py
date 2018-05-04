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
    driver.get("https://sturm.islandsville.com/admin/index.php")
    driver.implicitly_wait(4)
    email = driver.find_element_by_id('YumUserLogin_username')
    email.send_keys(ADMLOGIN)
    password = driver.find_element_by_id('YumUserLogin_password')
    password.send_keys(ADMPASS)
    log = driver.find_element_by_name('yt0')
    log.click()

    # Loading a dump
    driver.get("https://sturm.islandsville.com/admin/index.php?r=users/dump")
    user = driver.find_element_by_name('MDump[user]')
    user.click()
    user.send_keys('VK7777')
    loadlist = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[1]/td[3]/a')
    loadlist.click()
    checkbox = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[3]/td/input')
    checkbox.click()
    level = driver.find_element_by_xpath('//*[@id="s_dump"]/option[5]')
    level.click()
    usertwo = driver.find_element_by_name('MDump[t_user]')
    usertwo.click()
    usertwo.send_keys('FB185783681924469')
    checkboxtwo = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[3]/td/div/select/option[2]')
    checkboxtwo.click()
    loaddump = driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[4]/td[2]/a[1]/span')
    loaddump.click()
    time.sleep(3)
    movesleep2()
    time.sleep(1)
    okbutton = pyautogui.locateOnScreen('C:\Automation\Screens\Enixan_Admin_Panel\ok.png')
    tokbutton = pyautogui.center(okbutton)
    time.sleep(1)
    pyautogui.click(tokbutton)
    driver.close()

