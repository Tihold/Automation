import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from totem_tutorial import tutor_start_time


# Creating error class
class ErrorsTutorial:
    def __init__(self, test_name, start_time):
        self.test_name = test_name
        self.start_time = start_time

    def error_tutorial(self):
        test_name = self.test_name
        test_failure_time = datetime.now()
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        run_time = test_failure_time - self.start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Totem_tutorial_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + str(test_name) + 'failed in: ' + str(timenow2) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()
        driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        driver.quit()

def tutor_error():
    tutor_error_var = ErrorsTutorial('Test run Totem tutorial ', tutor_start_time)
    tutor_error_var.error_tutorial()