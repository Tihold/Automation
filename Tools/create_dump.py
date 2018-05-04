import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts import ADMLOGIN, ADMPASS


class Dump(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://sturm.islandsville.com/admin/index.php")
        self.driver.implicitly_wait(4)
        email = self.driver.find_element_by_id('YumUserLogin_username')
        email.send_keys (ADMLOGIN)
        password = self.driver.find_element_by_id('YumUserLogin_password')
        password.send_keys(ADMPASS)
        log = self.driver.find_element_by_name('yt0')
        log.click()

    def test_create_dump(self):
        # Create dump of user progress
        self.driver.get("https://sturm.islandsville.com/admin/index.php?r=users/dump")
        user = self.driver.find_element_by_name('MDump[user]')
        user.click()
        user.send_keys('VK777')
        loadlist = self.driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[1]/td[3]/a')
        loadlist.click()
        checkbox = self.driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[3]/td/input')
        checkbox.click()
        usertwo = self.driver.find_element_by_name('MDump[t_user]')
        usertwo.click()
        usertwo.send_keys('VK777')
        create = self.driver.find_element_by_xpath('//*[@id="dump-form"]/tbody/tr[4]/td[2]/a[2]/span')
        create.click()

if __name__ == "__main__":
    unittest.main()