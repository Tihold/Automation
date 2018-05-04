import sys
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from tf_preserves_50k import start_time_preserves_50k
from tf_preserves_5k import start_time_preserves_5k
from tf_preserves_350 import start_time_preserves_350
from tf_preserves_100 import start_time_preserves_100
from tf_oil_50k import start_time_oil_50k
from tf_oil_5k import start_time_oil_5k
from tf_oil_350 import start_time_oil_350
from tf_oil_100 import start_time_oil_100
from tf_materials_50k import start_time_materials_50k
from tf_materials_5k import start_time_materials_5k
from tf_materials_350 import start_time_materials_350
from tf_materials_100 import start_time_materials_100
from tf_steel_50k import start_time_steel_50k
from tf_steel_5k import start_time_steel_5k
from tf_steel_350 import start_time_steel_350
from tf_steel_100 import start_time_steel_100
sys.path.insert(0, 'C:\Automation\Tools')

# Creating the error class
class ResourceErrors:
    def __init__(self, test_name, for_res, start_time):
        self.test_name = test_name
        self.for_res = for_res
        self.start_time = start_time

    def resources_error(self):
        test_name = self.test_name
        for_res = self.for_res
        test_failure_time = datetime.now()
        timenow = datetime.now()
        timenow1 = str(timenow)
        timenow2 = (timenow1[:-7])
        run_time = test_failure_time - self.start_time
        run_time1 = str(run_time)
        run_time2 = (run_time1[:-7])
        tf = r'C:\Total_Front_resources_Log.txt'
        f2 = open(tf, 'a')
        f2.write("***************************************************************" + '\n'
                 + str(test_name) + str(for_res) + 'failed in: ' + str(timenow2) + '\n'
                 + 'Test running time: ' + str(run_time2) + '\n'
                 + "***************************************************************" + '\n')
        f2.close()
        driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        driver.quit()

# Creating instances of the class
# for Preserves
def error_preserves_50k():
    error_preserves_50k_var = ResourceErrors('Test 1', ' (for Preserves = 50000) ', start_time_preserves_50k)
    error_preserves_50k_var.resources_error()

def error_preserves_5k():
    error_preserves_5k_var = ResourceErrors('Test 2', ' (for Preserves = 5000) ', start_time_preserves_5k)
    error_preserves_5k_var.resources_error()

def error_preserves_350():
    error_preserves_350_var = ResourceErrors('Test 3', ' (for Preserves = 350) ', start_time_preserves_350)
    error_preserves_350_var.resources_error()

def error_preserves_100():
    error_preserves_100_var = ResourceErrors('Test 4', ' (for Preserves = 100) ', start_time_preserves_100)
    error_preserves_100_var.resources_error()

# for Oil
def error_oil_50k():
    error_oil_50k_var = ResourceErrors('Test 1', ' (for Oil = 50000) ', start_time_oil_50k)
    error_oil_50k_var.resources_error()

def error_oil_5k():
    error_oil_5k_var = ResourceErrors('Test 2', ' (for Oil = 5000) ', start_time_oil_5k)
    error_oil_5k_var.resources_error()

def error_oil_350():
    error_oil_350_var = ResourceErrors('Test 3', ' (for Oil = 350) ', start_time_oil_350)
    error_oil_350_var.resources_error()

def error_oil_100():
    error_oil_100_var = ResourceErrors('Test 4', ' (for Oil = 100) ', start_time_oil_100)
    error_oil_100_var.resources_error()

# for Materials
def error_materials_50k():
    error_materials_50k_var = ResourceErrors('Test 1', ' (for Materials = 50000) ', start_time_materials_50k)
    error_materials_50k_var.resources_error()

def error_materials_5k():
    error_materials_5k_var = ResourceErrors('Test 2', ' (for Materials = 5000) ', start_time_materials_5k)
    error_materials_5k_var.resources_error()

def error_materials_350():
    error_materials_350_var = ResourceErrors('Test 3', ' (for Materials = 350) ', start_time_materials_350)
    error_materials_350_var.resources_error()

def error_materials_100():
    error_materials_100_var = ResourceErrors('Test 4', ' (for Materials = 100) ', start_time_materials_100)
    error_materials_100_var.resources_error()

# for Steel
def error_steel_50k():
    error_steel_50k_var = ResourceErrors('Test 1', ' (for Steel = 50000) ', start_time_steel_50k)
    error_steel_50k_var.resources_error()

def error_steel_5k():
    error_steel_5k_var = ResourceErrors('Test 2', ' (for Steel = 5000) ', start_time_steel_5k)
    error_steel_5k_var.resources_error()

def error_steel_350():
    error_steel_350_var = ResourceErrors('Test 3', ' (for Steel = 350) ', start_time_steel_350)
    error_steel_350_var.resources_error()

def error_steel_100():
    error_steel_100_var = ResourceErrors('Test 4', ' (for Steel = 100) ', start_time_steel_100)
    error_steel_100_var.resources_error()