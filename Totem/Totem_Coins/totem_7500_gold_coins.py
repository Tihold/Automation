import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from movesleeps import *
from accounts import ADMLOGIN, ADMPASS
from accounts import FBLOGIN, FBPASS
from totem_coins_errors import *
from imageclicker import *
from regions_locator import *
from totem_load_dump import *

test05_start_time = datetime.now()


class GoldenCoin(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()
        load_dumps()


    def test05_7500_golden_coins(self):
        # Log in to admin panel
        self.driver.get("http://tribe.islandsville.com/admin/index.php?r=user/auth")
        self.driver.implicitly_wait(4)
        email = self.driver.find_element_by_id('YumUserLogin_username')
        email.send_keys(ADMLOGIN)
        password = self.driver.find_element_by_id('YumUserLogin_password')
        password.send_keys(ADMPASS)
        log = self.driver.find_element_by_name('yt0')
        log.click()

        # Choosing the test user
        fbchoose = self.driver.find_element_by_xpath('//*[@id="adminbar"]/table/tbody/tr/td[1]/select[2]/option[3]')
        fbchoose.click()
        fbuseres = self.driver.find_element_by_xpath('//*[@id="yw4"]/li[1]/a')
        fbuseres.click()
        finduser = self.driver.find_element_by_xpath('//*[@id="Filter__id.string"]')
        finduser.click()
        finduser.send_keys('142075956295242')
        missclick = self.driver.find_element_by_xpath('//*[@id="Filter_aka.match"]')
        missclick.click()
        movesleep2()

        # Opening the warehouse
        fbstock = self.driver.find_element_by_xpath('//*[@id="yw0"]/table[2]/tbody/tr/td[8]/div/a[3]')
        fbstock.click()

        searching = self.driver.find_element_by_xpath(
            '//*[@id="test001"]/table/thead/tr[1]/td[3]/form/div/div/div[2]/div/span')
        searching.click()
        searching_input = self.driver.find_element_by_xpath(
            '//*[@id="test001"]/table/thead/tr[1]/td[3]/form/div/div/div[1]/input[2]')
        searching_input.send_keys('монеты')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)

        # Choosing the coins
        output = self.driver.find_element_by_xpath('//*[@id="output"]')
        output.click()
        coins = self.driver.find_element_by_xpath('//*[@id="input"]/input')
        time.sleep(1)

        # Recording the amount of coins
        coins_first = coins.get_attribute('value')
        coins_first_int = int(coins_first)

        # Opening the game
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

        # Clicking on the "Play" button
        self.splay = ImageClicker('C:\Automation\Screens\FB_Start\Tplay.png', 50,
                                  er_coins_test05, '\Automation\Reports\Totem\Totem_Coins\Golden\Test05_bug.png')
        self.splay.founder_and_clicker()

        # Clicking on the "Allow" button
        self.allow = ImageClicker('C:\Automation\Screens\FB_Start\Tallow.png', 50,
                                  er_coins_test05, '\Automation\Reports\Totem\Totem_Coins\Golden\Test05_bug.png')
        self.allow.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 220)")

        # Closing the daily rewards window
        self.allow = ImageClicker('C:\Automation\Screens\Totem\Coins\daylics_close.png', 50,
                                  er_coins_test05, '\Automation\Reports\Totem\Totem_Coins\Golden\Test05_bug.png')
        self.allow.founder_and_clicker()

        # Running locator script for searching "Plus" buttons and clicking the button with coins.
        self.plus_coins = RegionsLocator('C:\Automation\Screens\Totem\Coins\golden_plus.png', 50, er_coins_test05,
                                         '\Automation\Reports\Totem\Totem_Coins\Golden\Test05_bug.png', 1)
        self.plus_coins.find_xy_and_click()

        # Running locator script for searching necessary instance of "Buy" button and clicking on him.
        self.sbuy = RegionsLocator('C:\Automation\Screens\Totem\Coins\sbuy.png', 50, er_coins_test05,
                                   '\Automation\Reports\Totem\Totem_Coins\Golden\Test05_bug.png', 4)
        self.sbuy.find_xy_and_click()

        # Clicking on the "Buy" button in the Facebook API
        self.allow = ImageClicker('C:\Automation\Screens\Totem\Coins\sfb_api_buy.png', 50,
                                  er_coins_test05, '\Automation\Reports\Totem\Totem_Coins\Golden\Test05_bug.png')
        self.allow.founder_and_clicker()

        # Opening admin panel
        self.driver.get("http://tribe.islandsville.com/admin/index.php?r=user/auth")
        self.driver.implicitly_wait(4)

        # Choosing the test user
        facebook_users = self.driver.find_element_by_xpath('//*[@id="yw7"]/li[1]/a')
        facebook_users.click()
        finduser = self.driver.find_element_by_xpath('//*[@id="Filter__id.string"]')
        finduser.click()
        finduser.send_keys('142075956295242')
        missclick = self.driver.find_element_by_xpath('//*[@id="Filter_aka.match"]')
        missclick.click()
        movesleep2()

        # Opening the warehouse
        fbstock = self.driver.find_element_by_xpath('//*[@id="yw0"]/table[2]/tbody/tr/td[8]/div/a[3]')
        fbstock.click()

        searching = self.driver.find_element_by_xpath(
            '//*[@id="test001"]/table/thead/tr[1]/td[3]/form/div/div/div[2]/div/span')
        searching.click()
        searching_input = self.driver.find_element_by_xpath(
            '//*[@id="test001"]/table/thead/tr[1]/td[3]/form/div/div/div[1]/input[2]')
        searching_input.send_keys('монеты')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)

        # Choosing the coins
        output = self.driver.find_element_by_xpath('//*[@id="output"]')
        output.click()
        coins = self.driver.find_element_by_xpath('//*[@id="input"]/input')
        time.sleep(1)

        # Recording the amount of coins
        coins_second = coins.get_attribute('value')
        coins_second_int = int(coins_second)

        # Coins delta (normal 7500)
        coins_delta = coins_second_int - coins_first_int
        coins_delta_int = int(coins_delta)

        # Printing test result and time of ending in the log
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        end_time = datetime.now()
        run_time = end_time - test05_start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Totem_coins_Log.txt'
        f2 = open(tf, 'a')
        if coins_delta_int == 7500:
            f2.write("***************************************************************" + '\n'
                     + 'TEST 5 completed in: ' + str(timenow2) + '\n'
                     + 'Coins before: ' + str(coins_first_int) + '\n'
                     + 'Coins after: ' + str(coins_second_int) + '\n'
                     + 'Delta = ' + str(coins_delta) + '\n'
                     + 'Test running time: ' + str(run_time2) + '\n'
                     + "***************************************************************" + '\n')
            f2.close()
        else:
            er_coins_test05()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


