import sys
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from totem_200000_gold_coins import test01_start_time
from totem_100000_gold_coins import test02_start_time
from totem_40000_gold_coins import test03_start_time
from totem_15000_gold_coins import test04_start_time
from totem_7500_gold_coins import test05_start_time
from totem_3000_gold_coins import test06_start_time
sys.path.insert(0, 'C:\Automation\Tools')

# Creating the error class
class ErrorsCoins:
    def __init__(self, test_name, for_coins, start_time):
        self.test_name = test_name
        self.for_coins = for_coins
        self.start_time = start_time

    def coins_error(self):
        test_name = self.test_name
        for_coins = self.for_coins
        test_failure_time = datetime.now()
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        run_time = test_failure_time - self.start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Totem_coins_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + str(test_name) + str(for_coins) + 'failed in: ' + str(timenow2) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()
        driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        driver.quit()

# Creating instances of the class
def er_coins_test01():
    er_gold_coins_200000_var = ErrorsCoins('Test 1', ' (for coins = 200000) ', test01_start_time)
    er_gold_coins_200000_var.coins_error()

def er_coins_test02():
    er_gold_coins_100000_var = ErrorsCoins('Test 2', ' (for coins = 100000) ', test02_start_time)
    er_gold_coins_100000_var.coins_error()

def er_coins_test03():
    er_gold_coins_40000_var = ErrorsCoins('Test 3', ' (for coins = 40000) ', test03_start_time)
    er_gold_coins_40000_var.coins_error()

def er_coins_test04():
    er_gold_coins_15000_var = ErrorsCoins('Test 4', ' (for coins = 15000) ', test04_start_time)
    er_gold_coins_15000_var.coins_error()

def er_coins_test05():
    er_gold_coins_7500_var = ErrorsCoins('Test 5', ' (for coins = 7500) ', test05_start_time)
    er_gold_coins_7500_var.coins_error()

def er_coins_test06():
    er_gold_coins_3000_var = ErrorsCoins('Test 6', ' (for coins = 3000) ', test06_start_time)
    er_gold_coins_3000_var.coins_error()