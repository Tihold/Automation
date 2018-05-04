import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts import ADMLOGIN, ADMPASS
from movesleeps import *


def delete_user():
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

    # Choosing the test user
    fbchoose = driver.find_element_by_xpath('//*[@id="adminbar"]/table/tbody/tr/td[1]/select[2]/option[2]')
    fbchoose.click()
    fbuseres = driver.find_element_by_xpath('//*[@id="yw1"]/li[1]/a')
    fbuseres.click()
    finduser = driver.find_element_by_id('Filter__id.match')
    finduser.send_keys('185783681924469')
    missclick = driver.find_element_by_xpath('// *[ @ id = "Filter_aka.match"]')
    missclick.click()
    movesleep2()

    # Deleting the test user
    deletebutton = driver.find_element_by_xpath('//*[@id="yw0"]/table[2]/tbody/tr/td[15]/div/a[10]')
    deletebutton.click()
    movesleep2()
    okbutton = pyautogui.locateOnScreen('C:\Automation\Screens\Enixan_Admin_Panel\ok.png')
    tokbutton = pyautogui.center(okbutton)
    pyautogui.click(tokbutton)
    movesleep2()
    driver.close()
