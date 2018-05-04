import sys
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from tf_tutorial import start_time_tutorial
sys.path.insert(0, 'C:\Automation\Tools')

# Creating the error class
class TutorialErrors:
    def __init__(self, test_name, for_tutor, start_time):
        self.test_name = test_name
        self.for_tutor = for_tutor
        self.start_time = start_time

    def tutorial_error(self):
        test_name = self.test_name
        for_tutor = self.for_tutor
        test_failure_time = datetime.now()
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        run_time = test_failure_time - self.start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Total_Front_tutorial_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + str(test_name) + str(for_tutor) + 'failed in: ' + str(timenow2) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()
        driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        driver.quit()

# Creating instances of the class
def error_tutorial():
    error_tutorial_var = TutorialErrors('Test 1', ' (for TF tutorial) ', start_time_tutorial)
    error_tutorial_var.tutorial_error()