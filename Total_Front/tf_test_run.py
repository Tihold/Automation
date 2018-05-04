import sys
sys.path.insert(0, 'C:\Automation\Tools')
sys.path.insert(0, 'C:\Automation\Total_Front\Total_Front_Gold')
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts import ADMLOGIN, ADMPASS, FBLOGIN, FBPASS
from datetime import datetime
from movesleeps import *
from load_dump import *
from tf_gold_errors import *
from imageclicker import *

start_time1000 = datetime.now()


class VIP(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()


    def test01_tf_run(self):
        # Opening the game
        self.driver.get("https://www.facebook.com/")
        self.driver.implicitly_wait(4)
        email = self.driver.find_element_by_id('email')
        email.send_keys(FBLOGIN)
        password = self.driver.find_element_by_id('pass')
        password.send_keys(FBPASS)
        log = self.driver.find_element_by_id('loginbutton')
        log.click()
        self.driver.get("https://apps.facebook.com/totalfront/")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        movesleep2()

        # Clicking to "Play" button
        self.splay = ImageClicker('C:\Automation\Screens\FB_Start\sigrat.png', 50,
                                  error_gold1000, '\Automation\Reports\Total_Front\GOLD\Test02_bug.png')
        self.splay.founder_and_clicker()

        # Clicking to "Allow" button
        self.allow = ImageClicker('C:\Automation\Screens\FB_Start\sallow.png', 50,
                                  error_gold1000, '\Automation\Reports\Total_Front\GOLD\Test02_bug.png')
        self.allow.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 250)")

if __name__ == "__main__":
    unittest.main()