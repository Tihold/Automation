import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts import ADMLOGIN, ADMPASS
from movesleeps import *
from imageclicker import *
from totem_tutorial_errors import *


def totem_delete_user():
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

    # Choosing the test user
    fbchoose = driver.find_element_by_xpath('//*[@id="adminbar"]/table/tbody/tr/td[1]/select[2]/option[3]')
    fbchoose.click()
    fbuseres = driver.find_element_by_xpath('//*[@id="yw4"]/li[1]/a')
    fbuseres.click()
    finduser = driver.find_element_by_xpath('//*[@id="Filter__id.string"]')
    finduser.click()
    finduser.send_keys('142075956295242')
    missclick = driver.find_element_by_xpath('//*[@id="Filter_aka.match"]')
    missclick.click()
    movesleep2()

    # Deleting the test user
    deletebutton = driver.find_element_by_xpath('//*[@id="yw0"]/table[2]/tbody/tr/td[8]/div/a[10]')
    deletebutton.click()
    movesleep2()
    sok = ImageClicker('C:\Automation\Screens\Enixan_Admin_Panel\ok.png', 50,
                       tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
    sok.founder_and_clicker()
    time.sleep(3)
    driver.close()
