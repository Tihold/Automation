import sys
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from total_front_gold2500 import start_time2500
from total_front_gold1000 import start_time1000
from total_front_gold350 import start_time350
from total_front_gold150 import start_time150
from total_front_gold60 import start_time60
from total_front_gold20 import start_time20
sys.path.insert(0, 'C:\Automation\Tools')

# Creating the error class
class ErrorsGold:
    def __init__(self, test_name, for_gold, start_time):
        self.test_name = test_name
        self.for_gold = for_gold
        self.start_time = start_time

    def gold_error(self):
        test_name = self.test_name
        for_gold = self.for_gold
        test_failure_time = datetime.now()
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        run_time = test_failure_time - self.start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Total_Front_Gold_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + str(test_name) + str(for_gold) + 'failed in: ' + str(timenow2) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()
        driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        driver.quit()

# Creating instances of the class
def error_gold2500():
    error_gold2500_var = ErrorsGold('Test 1', ' (for Gold = 2500) ', start_time2500)
    error_gold2500_var.gold_error()

def error_gold1000():
    error_gold1000_var = ErrorsGold('Test 2', ' (for Gold = 1000) ', start_time1000)
    error_gold1000_var.gold_error()

def error_gold350():
    error_gold350_var = ErrorsGold('Test 3', ' (for Gold = 350) ', start_time350)
    error_gold350_var.gold_error()

def error_gold150():
    error_gold150_var = ErrorsGold('Test 4', ' (for Gold = 150) ', start_time150)
    error_gold150_var.gold_error()

def error_gold60():
    error_gold60_var = ErrorsGold('Test 5', ' (for Gold = 60) ', start_time60)
    error_gold60_var.gold_error()

def error_gold20():
    error_gold20_var = ErrorsGold('Test 6', ' (for Gold = 20) ', start_time20)
    error_gold20_var.gold_error()

