import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from accounts import ADMLOGIN, ADMPASS, FBLOGIN, FBPASS
from movesleeps import *
from imageclicker import *
from totem_tutorial_errors import *

tutor_start_time = datetime.now()

class RUN(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        time.sleep(3)
        email = self.driver.find_element_by_id('email')
        email.send_keys(FBLOGIN)
        password = self.driver.find_element_by_id('pass')
        password.send_keys(FBPASS)
        log = self.driver.find_element_by_id('loginbutton')
        log.click()
        self.driver.get("https://apps.facebook.com/totemgame/?fb_source=search")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        movesleep2()

    def test01_run_totem(self):
        # Clicking to "Play" button
        self.splay = ImageClicker('C:\Automation\Screens\FB_Start\Tplay.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.splay.founder_and_clicker()

        # Clicking to "Allow" button
        self.allow = ImageClicker('C:\Automation\Screens\FB_Start\Tallow.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.allow.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 220)")




if __name__ == "__main__":
    unittest.main()