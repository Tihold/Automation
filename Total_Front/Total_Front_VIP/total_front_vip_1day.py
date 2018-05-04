import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts import ADMLOGIN, ADMPASS, FBLOGIN, FBPASS
from datetime import datetime
from movesleeps import *
from load_dump import *
from tf_vip_errors import *
from imageclicker import *


start_time1 = datetime.now()

class VIP(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()
        load_dumps()
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

        # Clicking to "Play" button
        self.splay = ImageClicker('C:\Automation\Screens\FB_Start\sigrat.png', 50,
                                  error_vip1, '\Automation\Reports\Total_Front\VIP\Test01_bug.png')
        self.splay.founder_and_clicker()

        # Clicking to "Allow" button
        self.allow = ImageClicker('C:\Automation\Screens\FB_Start\sallow.png', 50,
                                  error_vip1, '\Automation\Reports\Total_Front\VIP\Test01_bug.png')
        self.allow.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 250)")


    def test01_vip1day(self):
        # Closing the daily rewards window
        self.daylics = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_VIP\dailycs_close.png', 20,
                                    error_vip1, '\Automation\Reports\Total_Front\VIP\Test01_bug.png')
        self.daylics.founder_and_clicker()

        # Switching to full screen
        self.sfullscreen = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_VIP\sfullscreen.png', 50,
                                        error_vip1, '\Automation\Reports\Total_Front\VIP\Test01_bug.png')
        self.sfullscreen.founder_and_clicker()

        # Clicking "VIP" button
        self.svipsilver = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_VIP\svipsilver.png', 50,
                                       error_vip1, '\Automation\Reports\Total_Front\VIP\Test01_bug.png')
        self.svipsilver.founder_and_clicker()

        # Clicking to image of two dollars
        self.s2dollar = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_VIP\s2dollar.png', 50,
                                     error_vip1, '\Automation\Reports\Total_Front\VIP\Test01_bug.png')
        self.s2dollar.founder_and_clicker()

        # Confirmation of purchase in FB API
        time.sleep(7)
        self.sbuy = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_VIP\sbuy.png', 50,
                                 error_vip1, '\Automation\Reports\Total_Front\VIP\Test01_bug.png')
        self.sbuy.founder_and_clicker()

        # Log in to admin panel
        self.driver.get("https://sturm.islandsville.com/admin/index.php")
        self.driver.implicitly_wait(4)
        email = self.driver.find_element_by_id('YumUserLogin_username')
        email.send_keys(ADMLOGIN)
        password = self.driver.find_element_by_id('YumUserLogin_password')
        password.send_keys(ADMPASS)
        log = self.driver.find_element_by_name('yt0')
        log.click()

        # Choosing a test user
        fbchoose = self.driver.find_element_by_xpath('//*[@id="adminbar"]/table/tbody/tr/td[1]/select[2]/option[2]')
        fbchoose.click()
        fbusers = self.driver.find_element_by_xpath('//*[@id="yw1"]/li[1]/a')
        fbusers.click()
        finduser = self.driver.find_element_by_id('Filter__id.match')
        finduser.send_keys('185783681924469')
        missclick = self.driver.find_element_by_xpath('// *[ @ id = "Filter_aka.match"]')
        missclick.click()
        movesleep2()

        # Printing test result and time of ending in the log
        editbutton = self.driver.find_element_by_xpath('//*[@id="yw0"]/table[2]/tbody/tr/td[15]/div/a[8]')
        editbutton.click()
        vipendfield = self.driver.find_element_by_xpath('//*[@id="Users_vip_end"]')
        vipendfield.click()
        timevipend = vipendfield.get_attribute('value')
        t2 = int(timevipend)
        t3 = datetime.fromtimestamp(t2)
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        t4 = t3 - timenow
        timedelta = str(t4)
        timedelta1 = (timedelta[:-7])
        end_time = datetime.now()
        run_time = end_time - start_time1
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Total_Front_VIP_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + 'TEST 1 (VIP for 1 day) completed in: ' + str(timenow2) + '\n'
                 + 'VIP for: ' + str(timedelta1) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()







