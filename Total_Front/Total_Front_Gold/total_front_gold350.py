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
from tf_gold_errors import *
from imageclicker import *

start_time350 = datetime.now()


class VIP(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()
        load_dumps()

    def test03_350gold(self):
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
        fbstock = self.driver.find_element_by_xpath('// *[ @ id = "yw0"] / table[2] / tbody / tr / td[15] / div / a[3]')
        fbstock.click()
        filtersid = self.driver.find_element_by_xpath('//*[@id="Filter_sid.list"]')
        filtersid.click()
        fbstock.send_keys('22')
        missclick = self.driver.find_element_by_xpath('// *[ @ id = "Filter_title.preg"]')
        missclick.click()

        # Choosing the gold
        gsearch = self.driver.find_element_by_xpath('//*[@id="output"]')
        gsearch.click()
        gcount = self.driver.find_element_by_xpath('// *[ @ id = "input"] / input')

        # Recording the amount of gold
        goldfirst = gcount.get_attribute('value')
        goldfirstint = int(goldfirst)

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
                                  error_gold350, '\Automation\Reports\Total_Front\GOLD\Test03_bug.png')
        self.splay.founder_and_clicker()

        # Clicking to "Allow" button
        self.allow = ImageClicker('C:\Automation\Screens\FB_Start\sallow.png', 50,
                                  error_gold350, '\Automation\Reports\Total_Front\GOLD\Test03_bug.png')
        self.allow.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 250)")

        # Closing the daily rewards window
        self.daylics = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Gold\dailycs_close.png', 50,
                                    error_gold350, '\Automation\Reports\Total_Front\GOLD\Test03_bug.png')
        self.daylics.founder_and_clicker()

        # Switching to full screen
        self.sfullscreen = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Gold\sfullscreen.png', 50,
                                        error_gold350, '\Automation\Reports\Total_Front\GOLD\Test03_bug.png')
        self.sfullscreen.founder_and_clicker()

        # Clicking to "plus" button
        self.plus = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Gold\gold_choice.png', 50,
                                 error_gold350, '\Automation\Reports\Total_Front\GOLD\Test03_bug.png')
        self.plus.founder_and_clicker()

        # Clicking to image of 20 dollars
        self.imagedollars = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Gold\sgold20.png', 50,
                                         error_gold350, '\Automation\Reports\Total_Front\GOLD\Test03_bug.png')
        self.imagedollars.founder_and_clicker()

        # Buying a gold
        time.sleep(7)
        self.buygold = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Gold\skupit.png', 50,
                                    error_gold350, '\Automation\Reports\Total_Front\GOLD\Test03_bug.png')
        self.buygold.founder_and_clicker()

        '''
        Checking the value of gold after purchase
        '''

        # Open admin panel
        self.driver.get("https://sturm.islandsville.com/admin/index.php")
        self.driver.implicitly_wait(4)

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
        fbstock = self.driver.find_element_by_xpath('// *[ @ id = "yw0"] / table[2] / tbody / tr / td[15] / div / a[3]')
        fbstock.click()
        filtersid = self.driver.find_element_by_xpath('//*[@id="Filter_sid.list"]')
        filtersid.click()
        fbstock.send_keys('22')
        missclick = self.driver.find_element_by_xpath('// *[ @ id = "Filter_title.preg"]')
        missclick.click()

        # Choosing the gold
        gsearch = self.driver.find_element_by_xpath('//*[@id="output"]')
        gsearch.click()
        gcount = self.driver.find_element_by_xpath('// *[ @ id = "input"] / input')

        # Recording the amount of gold
        goldsecond = gcount.get_attribute('value')
        goldsecondint = int(goldsecond)

        # Gold delta (normal 350)
        golddelta = goldsecondint - goldfirstint
        golddelta1 = int(golddelta)

        # Printing test result and time of ending in the log
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        end_time = datetime.now()
        run_time = end_time - start_time350
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Total_Front_GOLD_Log.txt'
        f2 = open(tf, 'a')
        if golddelta1 == 350:
            f2.write("***************************************************************" + '\n'
                     + 'TEST 3 completed in: ' + str(timenow2) + '\n'
                     + 'Gold before: ' + str(goldfirstint) + '\n'
                     + 'Gold after: ' + str(goldsecondint) + '\n'
                     + 'Delta = ' + str(golddelta) + '\n'
                     + 'Test running time: ' + str(run_time2) + '\n'
                     + "***************************************************************" + '\n')
            f2.close()
        else:
            error_gold350()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()