import sys
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from tf_worker import start_time

sys.path.insert(0, 'C:\Automation\Tools')

# Creating the error class
class ErrorsWorker:
    def __init__(self, test_name, for_worker, start_time):
        self.test_name = test_name
        self.for_worker = for_worker
        self.start_time = start_time

    def worker_error(self):
        test_name = self.test_name
        for_worker = self.for_worker
        test_failure_time = datetime.now()
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        run_time = test_failure_time - self.start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Total_Front_worker_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + str(test_name) + str(for_worker) + 'failed in: ' + str(timenow2) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()
        driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        driver.quit()

# Creating instances of the class
def workers_error():
    error_workers_var = ErrorsWorker('Test 1', ' (for one worker) ', start_time)
    error_workers_var.worker_error()