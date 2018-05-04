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
from tf_resources_errors import *
from regions_locator import *
from imageclicker import *

start_time_preserves_350 = datetime.now()


class Resources(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()
        load_dumps()

    def test03_preserves_350(self):
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
        fbuseres = self.driver.find_element_by_xpath('//*[@id="yw1"]/li[1]/a')
        fbuseres.click()
        finduser = self.driver.find_element_by_id('Filter__id.match')
        finduser.send_keys('185783681924469')
        missclick = self.driver.find_element_by_xpath('// *[ @ id = "Filter_aka.match"]')
        missclick.click()
        movesleep2()

        # Opening the warehouse
        fb_stock = self.driver.find_element_by_xpath('//*[@id="yw0"]/table[2]/tbody/tr/td[15]/div/a[3]')
        fb_stock.click()
        filter_sid = self.driver.find_element_by_xpath('//*[@id="Filter_sid.list"]')
        filter_sid.click()
        filter_sid.send_keys('23')
        pyautogui.press('enter')
        time.sleep(1)

        # Choosing the preserves
        output = self.driver.find_element_by_xpath('//*[@id="output"]')
        output.click()
        resources = self.driver.find_element_by_xpath('//*[@id="input"]/input')
        time.sleep(1)

        # Recording the quantity of preserves
        resources_first = resources.get_attribute('value')
        resources_first_int = int(resources_first)

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
                                  error_preserves_350,
                                  '\Automation\Reports\Total_Front\RESOURCES\Test03_preserves_bug.png')
        self.splay.founder_and_clicker()

        # Clicking to "Allow" button
        self.allow = ImageClicker('C:\Automation\Screens\FB_Start\sallow.png', 50,
                                  error_preserves_350,
                                  '\Automation\Reports\Total_Front\RESOURCES\Test03_preserves_bug.png')
        self.allow.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 250)")

        # Closing the daily rewards window
        self.dailycs_close = ImageClicker('C:\Automation\Screens\Total_Front\TF_Resources\dailycs_close.png', 50,
                                          error_preserves_350,
                                          '\Automation\Reports\Total_Front\RESOURCES\Test03_preserves_bug.png')
        self.dailycs_close.founder_and_clicker()

        # Switching to full screen
        self.sfullscreen = ImageClicker('C:\Automation\Screens\Total_Front\TF_Resources\sfullscreen.png', 50,
                                        error_preserves_350,
                                        '\Automation\Reports\Total_Front\RESOURCES\Test03_preserves_bug.png')
        self.sfullscreen.founder_and_clicker()

        # Running locator script for searching "Plus" buttons and clicking the button with preserves.
        self.plus_coins = RegionsLocator('C:\Automation\Screens\Total_Front\TF_Resources\splus_button.png', 50,
                                         error_preserves_350,
                                         '\Automation\Reports\Total_Front\RESOURCES\Test03_preserves_bug.png', 0)
        self.plus_coins.find_xy_and_click()

        # Clicking to "25 Gold" button
        self.s25_gold = ImageClicker('C:\Automation\Screens\Total_Front\TF_Resources\s25_gold.png', 50,
                                      error_preserves_350,
                                      '\Automation\Reports\Total_Front\RESOURCES\Test03_preserves_bug.png')
        self.s25_gold.founder_and_clicker()

        # Open admin panel
        self.driver.get("https://sturm.islandsville.com/admin/index.php")
        self.driver.implicitly_wait(4)

        # Choosing a test user
        fb_choose = self.driver.find_element_by_xpath('//*[@id="adminbar"]/table/tbody/tr/td[1]/select[2]/option[2]')
        fb_choose.click()
        fb_users = self.driver.find_element_by_xpath('//*[@id="yw1"]/li[1]/a')
        fb_users.click()
        find_user = self.driver.find_element_by_id('Filter__id.match')
        find_user.send_keys('185783681924469')
        miss_click = self.driver.find_element_by_xpath('// *[ @ id = "Filter_aka.match"]')
        miss_click.click()
        movesleep2()

        # Opening the warehouse
        fb_stock = self.driver.find_element_by_xpath('//*[@id="yw0"]/table[2]/tbody/tr/td[15]/div/a[3]')
        fb_stock.click()
        filter_sid = self.driver.find_element_by_xpath('//*[@id="Filter_sid.list"]')
        filter_sid.click()
        filter_sid.send_keys('23')
        pyautogui.press('enter')
        time.sleep(1)

        # Choosing the preserves
        output = self.driver.find_element_by_xpath('//*[@id="output"]')
        output.click()
        resources = self.driver.find_element_by_xpath('//*[@id="input"]/input')
        time.sleep(1)

        # Recording the quantity of preserves
        resources_second = resources.get_attribute('value')
        resources_second_int = int(resources_second)

        # Preserves delta (normal = 350)
        resources_delta = resources_second_int - resources_first_int
        resources_delta_int = int(resources_delta)

        # Printing test result and time of ending in the log
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        end_time = datetime.now()
        run_time = end_time - start_time_preserves_350
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Total_Front_resources_Log.txt'
        f2 = open(tf, 'a')
        if resources_delta_int == 350:
            f2.write("***************************************************************" + '\n'
                     + 'TEST 3 completed in: ' + str(timenow2) + '\n'
                     + 'Preserves before: ' + str(resources_first_int) + '\n'
                     + 'Preserves after: ' + str(resources_second_int) + '\n'
                     + 'Delta = ' + str(resources_delta) + '\n'
                     + 'Test running time: ' + str(run_time2) + '\n'
                     + "***************************************************************" + '\n')
            f2.close()
        else:
            error_preserves_350()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()