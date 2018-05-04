#Search images for Pyautogui
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

def movesleep1():
    pyautogui.moveTo(400, 400)
    time.sleep(2)
    pyautogui.moveTo(550, 550)
    time.sleep(4)

def movesleep2():
    pyautogui.moveTo(400, 400)
    time.sleep(1)
    pyautogui.moveTo(400, 402)

def movesleep3():
    pyautogui.moveTo(150, 150)
    time.sleep(1)
    pyautogui.moveTo(152, 152)

def movesleep4():
    pyautogui.moveTo(300, 300, 1)
    pyautogui.moveTo(450, 410, 1)
    pyautogui.moveTo(420, 430, 1)
    pyautogui.moveTo(310, 532, 1)
    pyautogui.moveTo(600, 600, 1)
    pyautogui.moveTo(400, 400, 1)