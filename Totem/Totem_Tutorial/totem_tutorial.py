import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from movesleeps import *
from accounts import FBLOGIN, FBPASS
from totem_delete_user import *
from totem_tutorial_errors import *

tutor_start_time = datetime.now()


class Tutorial(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()
        totem_delete_user()
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

        # Clicking to "Play" button
        self.splay = ImageClicker('C:\Automation\Screens\FB_Start\Tplay.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.splay.founder_and_clicker()

        # Clicking to "Allow" button
        self.allow = ImageClicker('C:\Automation\Screens\FB_Start\Tallow.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.allow.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 300)")

    def test01_tutorial(self):
        # Clicking on the "Further" button
        self.sfurther = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sfurther.png', 50,
                                     tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sfurther.founder_and_clicker()

        # Clicking on the flower
        self.sflower = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sflower.png', 50,
                                    tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sflower.founder_and_clicker()

        # Clicking on the "Further" button
        self.sfurther = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sfurther.png', 50,
                                     tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sfurther.founder_and_clicker()

        # Clicking on the backpack
        self.sbackpack = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sbackpack.png', 50,
                                      tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sbackpack.founder_and_clicker()

        # Clicking on the "Help" button
        self.shelp = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\shelp.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.shelp.founder_and_clicker()

        # Clicking on the "Put" button
        self.spostavit = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\spostavit.png', 50,
                                      tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.spostavit.founder_and_clicker()

        # Pitch one's tent
        time.sleep(5)
        self.stent_zone = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\stent_zone.png', 50,
                                       tutor_error, 'Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.stent_zone.founder_for_movesleep3()

        # Searching for portable radio on drop zone
        time.sleep(10)
        movesleep4()

        # Clicking on the "Further" button
        self.sfurther = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sfurther.png', 50,
                                     tutor_error, 'Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sfurther.founder_and_clicker()

        # Clicking on the "Help" button
        self.shelp = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\shelp.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.shelp.founder_and_clicker()

        # Collecting firewood
        self.sfirewood = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sfirewood.png', 50,
                                      tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sfirewood.founder_and_clicker()

        # Clicking on the "Help" button
        self.shelp = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\shelp.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.shelp.founder_and_clicker()

        # Clicking on the ananas
        self.sananas = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sananas.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sananas.founder_and_clicker()

        # Clicking on the "Help" button
        self.shelp = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\shelp.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.shelp.founder_and_clicker()

        # Clicking on water
        self.water = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\water.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.water.founder_and_clicker()

        # Clicking on the "Further" button
        self.sfurther = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sfurther.png', 50,
                                     tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sfurther.founder_and_clicker()

        # Clicking on the "Further" button
        self.sfurther = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sfurther.png', 50,
                                     tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sfurther.founder_and_clicker()

        # Clicking on the "Excellent" button
        self.excellent = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\excellent.png', 50,
                                      tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.excellent.founder_and_clicker()

        #  Clicking on the "Proceed" button
        self.sproceed = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sproceed.png', 50,
                                      tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sproceed.founder_and_clicker()

        # Clicking on the "Help" button
        self.shelp = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\shelp.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.shelp.founder_and_clicker()

        # Clicking on the "Improve" button
        self.simprove = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\simprove.png', 50,
                                     tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.simprove.founder_and_clicker()

        # Clicking on the "Help" button
        self.shelp = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\shelp.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.shelp.founder_and_clicker()

        # Clicking on the cookies
        self.scookies = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\scookies.png', 50,
                                     tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.scookies.founder_and_clicker()

        # Clicking on the "Create" button
        self.screate = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\screate.png', 50,
                                    tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.screate.founder_and_clicker()

        # Clicking on the "Thank" button
        self.sthank = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sthank.png', 50,
                                   tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sthank.founder_and_clicker()

        # Clicking on the "Thank" button in the quest pop-up window
        self.sthankquest = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sthankquest.png', 50,
                                        tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sthankquest.founder_and_clicker()

        # Clicking on the "Fine!" button
        self.sfine = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sfine.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sfine.founder_and_clicker()

        # Clicking on the "Help" button
        self.shelp = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\shelp.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.shelp.founder_and_clicker()

        # Clicking on the "Speed up" button
        self.speedup = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\speedup.png', 50,
                                    tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.speedup.founder_and_clicker()

        # Clicking on the "Thank" button
        self.sthank = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sthank.png', 50,
                                   tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sthank.founder_and_clicker()

        # Clicking on the "Fine!" button
        self.sfine = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sfine.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sfine.founder_and_clicker()

        # Clicking on the "Good" button in the quest pop-up window
        self.sgood = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sgood.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sgood.founder_and_clicker()

        # Sending an aborigine to collect bamboo
        self.sbambuk = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sbambuk.png', 50,
                                    tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sbambuk.founder_and_clicker()

        # Clicking on the "Good" button in the quest pop-up window
        self.sgood = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sgood.png', 50,
                                  tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sgood.founder_and_clicker()

        # Clicking on the "Thank" button
        self.sthank = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\sthank.png', 50,
                                   tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.sthank.founder_and_clicker()

        # Clicking on the "Excellent" button
        self.excellent = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\excellent.png', 50,
                                      tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.excellent.founder_and_clicker()

        # Clicking on the zero reward "Thanks" button
        self.szerothanks = ImageClicker('C:\Automation\Screens\Totem\Totem_tutorial\szerothanks.png', 50,
                                        tutor_error, '\Automation\Reports\Totem\Totem_tutorial\Test01_bug.png')
        self.szerothanks.founder_and_clicker()

        # Printing test result and time of ending in the log
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        end_time = datetime.now()
        run_time = end_time - tutor_start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Totem_tutorial_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + 'TEST Totem tutorial completed in: ' + str(timenow2) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

