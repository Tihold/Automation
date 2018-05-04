import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from total_front_vip_1day import start_time1
from total_front_vip_7days import start_time7
from total_front_vip_30days import start_time30

# Creating error class
class ErrorsVIP:
    def __init__(self, test_name, for_vip, start_time):
        self.test_name = test_name
        self.for_vip = for_vip
        self.start_time = start_time

    def vip_error(self):
        test_name = self.test_name
        for_vip = self.for_vip
        test_failure_time = datetime.now()
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        run_time = test_failure_time - self.start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Total_Front_VIP_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + str(test_name) + str(for_vip) + 'failed in: ' + str(timenow2) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()
        driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        driver.quit()


def error_vip1():
    error_vip1_var = ErrorsVIP('Test 1', ' (for VIP = 1 day) ', start_time1)
    error_vip1_var.vip_error()

def error_vip7():
    error_vip7_var = ErrorsVIP('Test 2', ' (for VIP = 7 days) ', start_time7)
    error_vip7_var.vip_error()

def error_vip30():
    error_vip30_var = ErrorsVIP('Test 3', ' (for VIP = 30 days) ', start_time30)
    error_vip30_var.vip_error()

