import sys
sys.path.insert(0, 'C:\Automation\Tools')
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from movesleeps import *

# Clicking on center of image
class ImageClicker:
    def __init__(self, image_path, measurer, raise_error, bug_rep_path, image=None, click_to_image=None):
        self.image_path = image_path
        self.measurer = measurer
        self.raise_error = raise_error
        self.bug_rep_path = bug_rep_path
        self.image = image
        self.click_to_image = click_to_image

    def founder_and_clicker(self):
        time.sleep(1)
        movesleep2()
        self.image = pyautogui.locateOnScreen(self.image_path)
        if self.image is not None:
            self.click_to_image = pyautogui.center(self.image)
            pyautogui.click(self.click_to_image)
            pass
        if self.image is None:
            while self.measurer > 0:
                movesleep2()
                self.image = pyautogui.locateOnScreen(self.image_path)
                self.measurer -= 1
                if self.image is not None:
                    self.click_to_image = pyautogui.center(self.image)
                    pyautogui.click(self.click_to_image)
                    break
                elif self.measurer > 0:
                    continue
                elif self.measurer == 0:
                    pass
        if self.measurer == 0:
            pyautogui.screenshot(self.bug_rep_path)
            self.raise_error()
            raise Exception('Test failed')

    def founder_for_movesleep3(self):
        time.sleep(1)
        movesleep3()
        self.image = pyautogui.locateOnScreen(self.image_path)
        if self.image is not None:
            self.click_to_image = pyautogui.center(self.image)
            pyautogui.click(self.click_to_image)
            pyautogui.doubleClick()
        if self.image is None:
            while self.measurer > 0:
                movesleep3()
                self.image = pyautogui.locateOnScreen(self.image_path)
                self.measurer -= 1
                if self.image is not None:
                    self.click_to_image = pyautogui.center(self.image)
                    pyautogui.click(self.click_to_image)
                    pyautogui.doubleClick()
                    break
                elif self.measurer > 0:
                    continue
                elif self.measurer == 0:
                    pass
        if self.measurer == 0:
            pyautogui.screenshot(self.bug_rep_path)
            self.raise_error()
            raise Exception('Test failed')

    def arrow_clicker(self):
        time.sleep(1)
        movesleep2()
        self.image = pyautogui.locateOnScreen(self.image_path)
        if self.image is not None:
            self.click_to_image = pyautogui.center(self.image)
            pyautogui.moveTo(self.click_to_image)
            pyautogui.doubleClick(self.click_to_image)
        if self.image is None:
            while self.measurer > 0:
                movesleep2()
                self.image = pyautogui.locateOnScreen(self.image_path)
                self.measurer -= 1
                if self.image is not None:
                    self.click_to_image = pyautogui.center(self.image)
                    pyautogui.moveTo(self.click_to_image)
                    pyautogui.doubleClick(self.click_to_image)
                    break
                elif self.measurer > 0:
                    continue
                elif self.measurer == 0:
                    pass
        if self.measurer == 0:
            pyautogui.screenshot(self.bug_rep_path)
            self.raise_error()
            raise Exception('Test failed')

