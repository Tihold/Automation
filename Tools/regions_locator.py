import sys
sys.path.insert(0, 'C:\Automation\Tools')
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from movesleeps import *

class RegionsLocator:
    def __init__(self, image_path, measurer, raise_error, bug_rep_path, image_instance):
        self.image_path = image_path
        self.measurer = measurer
        self.raise_error = raise_error
        self.bug_rep_path = bug_rep_path
        self.image_instance = image_instance

    def find_xy_and_click(self):
        movesleep2()
        all_found_coordinates = list(pyautogui.locateAllOnScreen(self.image_path))
        if all_found_coordinates:
            coordinates = list(all_found_coordinates[self.image_instance])
            x = int(coordinates[0])
            y = int(coordinates[1])
            pyautogui.click(x, y)
            pass
        if not all_found_coordinates:
            while self.measurer > 0:
                movesleep2()
                all_found_coordinates = list(pyautogui.locateAllOnScreen(self.image_path))
                self.measurer -= 1
                if all_found_coordinates:
                    coordinates = list(all_found_coordinates[self.image_instance])
                    x = int(coordinates[0])
                    y = int(coordinates[1])
                    pyautogui.click(x, y)
                    break
                elif self.measurer > 0:
                    continue
                elif self.measurer == 0:
                    pass
        if self.measurer == 0:
            pyautogui.screenshot(self.bug_rep_path)
            self.raise_error()
            raise Exception('Test failed')










