import sys
sys.path.insert(0, 'C:\Automation\Tools')
import unittest
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from movesleeps import *
from accounts import FBLOGIN, FBPASS
from delete_user import delete_user
from detect_nation import *
from tf_tutorial_error import *
from regions_locator import *
from imageclicker import *

start_time_tutorial = datetime.now()

class Tutorial(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='C:\Automation\chromedriver.exe')
        self.driver.maximize_window()
        delete_user()
        self.driver.get("https://www.facebook.com/")
        self.driver.implicitly_wait(4)
        email = self.driver.find_element_by_id('email')
        email.send_keys(FBLOGIN)
        password = self.driver.find_element_by_id('pass')
        password.send_keys(FBPASS)
        log = self.driver.find_element_by_id('loginbutton')
        log.click()
        self.driver.get("https://apps.facebook.com/totalfront/")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Clicking to "Play" button
        self.splay = ImageClicker('C:\Automation\Screens\FB_Start\sigrat.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.splay.founder_and_clicker()

        # Clicking to "Allow" button
        self.allow = ImageClicker('C:\Automation\Screens\FB_Start\sallow.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.allow.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 350)")

    def test_tutorial(self):
        # Поворот списка наций вправо
        self.sright = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sright.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sright.founder_and_clicker()

        # Поворот списка наций влево
        self.sleft = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sleft.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sleft.founder_and_clicker()

        # Выбор нации
        self.snation_button = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\snation_button.png',
                                           50, error_tutorial,
                                           '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.snation_button.founder_and_clicker()

        # Запуск скрипта для определения выбранной игроком нации и импорт этого значения.
        detect_nation()
        from detect_nation import nation as nation

        '''
                               *** Стартовая миссия ***
        '''
        # Нажатие кнопки "В атаку!"
        self.attack_button = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sattack_button.png',
                                          50, error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.attack_button.founder_and_clicker()

        # Нажатие кнопки "Далее"
        self.snext = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\snext.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.snext.founder_and_clicker()

        '''
                                *** Первый переход на ферму ***
        '''

        # Нажатие кнопки "Продолжить "
        self.scontinue = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scontinue.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scontinue.founder_and_clicker()

        # Нажатие кнопки "Приступить  "
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()

        #Нажатие на иконку "Магазина"
        self.sstorebutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sstorebutton.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sstorebutton.founder_and_clicker()

        # Нажатие на иконку "Купить"
        self.sbuybutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sbuybutton.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sbuybutton.founder_and_clicker()

        # Выставление здания (клик по стрелке)
        self.sclickto = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sclickto.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sclickto.arrow_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgood = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgood.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgood.founder_and_clicker()

        # Сбор консервов
        self.sspam = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sspam.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sspam.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgood = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgood.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgood.founder_and_clicker()

        # Найм стрелков (клик по иконке стрелка соответствующей нации)
        self.driver.execute_script("window.scrollTo(0, 300)")
        if nation == '3': # Советы
            self.susoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\susoldier.png', 50,
                                          error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.susoldier.founder_and_clicker()
        elif nation == '1': # США
            self.sussoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sussoldier.png', 50,
                                           error_tutorial,
                                           '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.sussoldier.founder_and_clicker()
        elif nation == '2': # Британия
            self.gbsoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\gbsoldier.png', 50,
                                          error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.gbsoldier.founder_and_clicker()
        elif nation == '4': # Рейх
            self.sresoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sresoldier.png', 50,
                                           error_tutorial,
                                           '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.sresoldier.founder_and_clicker()
        elif nation == '5': # Италия
            self.itsoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\itsoldier.png', 50,
                                          error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.itsoldier.founder_and_clicker()
        elif nation == '6': # Япония
            self.jpsoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\jpsoldier.png', 50,
                                          error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.jpsoldier.founder_and_clicker()
        else:
            error_tutorial()

        # Нажатие кнопки "Приступить  "
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()

        # Клик по казарме
        self.sbarracks = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sbarracks.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sbarracks.founder_and_clicker()

        # Найм стрелков
        self.shire = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\shire.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.shire.founder_and_clicker()

        # Ускорение за харду
        self.sgoldfast = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoldfast.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoldfast.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgood = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgood.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgood.founder_and_clicker()

        # Нажатие на иконку миссии
        self.smissionicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissionicon.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.smissionicon.founder_and_clicker()

        # Нажатие на кнопку "Приступить" и скролл вниз
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        # Нажатие на иконку компании в меню и скролл вверх
        self.scompanyicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scompanyicon.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scompanyicon.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 300)")

        # Нажатие на иконку компании
        self.sfirstcomp = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sfirstcomp.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sfirstcomp.founder_and_clicker()

        # Нажатие на иконку компании на карте компаний
        self.sgreenicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgreenicon.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgreenicon.founder_and_clicker()


        # Нажатие на кнопку "Начать"
        self.start_button = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\start_button.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.start_button.founder_and_clicker()

        # Нажатие кнопки "В атаку!"
        self.attack_button = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sattack_button.png',
                                          50, error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.attack_button.founder_and_clicker()

        # Нажатие кнопки "Далее"
        self.snext = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\snext.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.snext.founder_and_clicker()

        # Нажатие кнопки "Продолжить "
        self.scontinue = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scontinue.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scontinue.founder_and_clicker()

        # Выбор иконки стрелка
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if nation == '3': # Советы
            self.susoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smisssurifle.png', 50,
                                          error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.susoldier.founder_and_clicker()
            self.driver.execute_script("window.scrollTo(0, 250)")
        elif nation == '1': # США
            self.sussoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissusarifle.png',
                                           50, error_tutorial,
                                           '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.sussoldier.founder_and_clicker()
            self.driver.execute_script("window.scrollTo(0, 250)")
        elif nation == '2': # Британия
            self.gbsoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissgbrifle.png', 50,
                                          error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.gbsoldier.founder_and_clicker()
            self.driver.execute_script("window.scrollTo(0, 250)")
        elif nation == '4': # Рейх
            self.sresoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissreichrifle.png',
                                           50, error_tutorial,
                                           '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.sresoldier.founder_and_clicker()
            self.driver.execute_script("window.scrollTo(0, 250)")
        elif nation == '5': # Италия
            self.itsoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissitrifle.png', 50,
                                          error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.itsoldier.founder_and_clicker()
            self.driver.execute_script("window.scrollTo(0, 250)")
        elif nation == '6': # Япония
            self.jpsoldier = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissjprifle.png', 50,
                                          error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.jpsoldier.founder_and_clicker()
            self.driver.execute_script("window.scrollTo(0, 250)")
        else:
            error_tutorial()

        # (клик по стрелке) и скролл вверх
        self.sclickto = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sclickto.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sclickto.founder_and_clicker()

        # Нажатие иконки артобстрела
        self.sarta = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sarta.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sarta.founder_and_clicker()

        # Нажатие на стрелку 2 и скролл вниз
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        '''
                                    *** Второй переход на ферму ***
        '''
        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на амбар и скролл вверх
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.sfactory = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sfactory.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sfactory.founder_and_clicker()

        # Нажатие на кнопку "Приступить" и скролл вниз
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Нажатие на иконку "Магазина"
        self.sstorebutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sstorebutton.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sstorebutton.founder_and_clicker()

        # Нажатие на иконку "Купить"
        self.sbuybutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sbuybutton.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sbuybutton.founder_and_clicker()


        # Нажатие на вторую стрелку и скролл вверх #### Здесь мб нужен двойной клик
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.arrow_clicker()

        # Нажатие на кнопку хорошо
        self.sgood = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgood.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgood.founder_and_clicker()

        # Нажатие на палатку
        self.stent = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\stent.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.stent.founder_and_clicker()

        # Нажатие на кнопку "Приступить" и скролл вниз
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Нажатие на иконку "Магазина"
        self.sstorebutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sstorebutton.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sstorebutton.founder_and_clicker()

        # Нажатие на иконку "Купить"
        self.sbuybutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sbuybutton.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sbuybutton.founder_and_clicker()

        # Скролл вверх и нажатие на 4 стрелку
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.sblue4 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue4.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue4.arrow_clicker()

        # Нажатие на кнопку хорошо
        self.sgood = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgood.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgood.founder_and_clicker()

        # Нажатие кнопки "Продолжить "
        self.scontinue = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scontinue.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scontinue.founder_and_clicker()

        # Нажатие на иконку миссии
        self.smissionicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissionicon.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.smissionicon.founder_and_clicker()

        # Нажатие на кнопку "Приступить"
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()

        # Нажатие на иконку миссии и скролл вниз
        self.smissionicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissionicon.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.smissionicon.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Нажатие на иконку компании в меню и скролл вверх
        self.scompanyicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scompanyicon.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scompanyicon.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 250)")

        # Нажатие на иконку компании
        self.sfirstcomp = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sfirstcomp.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sfirstcomp.founder_and_clicker()

        # Нажатие на иконку компании на карте компаний
        self.sgreenicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgreenicon.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgreenicon.founder_and_clicker()

        # Нажатие на кнопку "Начать"
        self.start_button = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\start_button.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.start_button.founder_and_clicker()

        # Нажатие кнопки "В атаку!"
        self.attack_button = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sattack_button.png',
                                          50, error_tutorial,
                                          '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.attack_button.founder_and_clicker()

        # Нажатие кнопки "Продолжить "
        self.scontinue = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scontinue.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scontinue.founder_and_clicker()

        # Выбор гранатометчиков
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if nation == '3':  # Советы
            self.ssugran = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\ssugran.png', 50,
                                        error_tutorial,
                                        '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.ssugran.founder_for_movesleep3()
        elif nation == '1':  # США
            self.susagran = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\susagran.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.susagran.founder_for_movesleep3()
        elif nation == '2':  # Британия
            self.sgbgran = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgbgran.png', 50,
                                        error_tutorial,
                                        '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.sgbgran.founder_for_movesleep3()
        elif nation == '4':  # Рейх
            self.sregran = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sregran.png', 50,
                                        error_tutorial,
                                        '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.sregran.founder_for_movesleep3()
        elif nation == '5':  # Италия
            self.sitgran = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sitgran.png', 50,
                                        error_tutorial,
                                        '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.sitgran.founder_for_movesleep3()
        elif nation == '6':  # Япония
            self.sjpgran = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sjpgran.png', 50,
                                        error_tutorial,
                                        '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
            self.sjpgran.founder_for_movesleep3()
        else:
            error_tutorial()

        # Скролл вверх и нажатие на стрелку 2
        self.driver.execute_script("window.scrollTo(0, 250)")
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.arrow_clicker()

        # Скролл вверх и нажатие на кнопку "Хорошо"
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на иконку миссии "Расчистка территории"
        self.stree = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\stree.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.stree.founder_and_clicker()

        # Нажатие на кнопку "Приступить"
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()

        # Нажатие на стрелку 2
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.arrow_clicker()

        # Нажатие на кнопку "Открыть"
        self.sopen = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sopen.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sopen.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на иконку квеста аеропорта
        self.saero = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\saero.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.saero.founder_and_clicker()

        # Нажатие на кнопку "Приступить"
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()

        # Нажатие на аеропорт
        self.saerobroken = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\saerobroken.png', 50,
                                        error_tutorial,
                                        '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.saerobroken.founder_and_clicker()

        # Восстановление аэропорта
        self.srebuild = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\srebuild.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.srebuild.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на кнопку "Приступить"
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()

        # Нажатие на самолет с ресурсами
        time.sleep(25)
        pyautogui.moveTo(520, 431)
        pyautogui.click()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на иконку квеста истребитель
        self.sfighter = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sfighter.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sfighter.founder_and_clicker()

        # Нажатие на кнопку "Приступить"
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()

        # Нажатие на стрелку 2
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.arrow_clicker()

        # Нажатие на кнопку "Создать"
        self.screate = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\screate.png', 50,
                                    error_tutorial,
                                    '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.screate.founder_and_clicker()

        # Ускорение за харду
        self.sgolda = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgolda.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgolda.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на иконку миссии
        self.smissionicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\smissionicon.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.smissionicon.founder_and_clicker()

        # Нажатие на кнопку "Приступить" и скролл вниз
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Нажатие на иконку компании в меню и скролл вверх
        self.scompanyicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scompanyicon.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scompanyicon.founder_and_clicker()

        # Нажатие на иконку компании
        self.sfirstcomp = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sfirstcomp.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sfirstcomp.founder_and_clicker()

        # Нажатие на иконку компании на карте компаний
        self.sgreenicon = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgreenicon.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgreenicon.founder_and_clicker()

        # Нажатие на кнопку "Начать"
        self.start_button = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\start_button.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.start_button.founder_and_clicker()

        # Выбор стрелков
        time.sleep(60)
        pyautogui.moveTo(372, 721)
        pyautogui.click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(3)

        # Нажатие на стрелки и скролл вверх
        time.sleep(5)
        pyautogui.moveTo(550, 435)
        pyautogui.click()
        time.sleep(10)
        pyautogui.moveTo(662, 471)
        pyautogui.click()
        self.driver.execute_script("window.scrollTo(0, 300)")

        # Нажатие на кнопку "В бой"
        self.sinbattle = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\ssinbattle.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sinbattle.founder_and_clicker()

        # Нажатие на приказ
        self.sinbattle = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\ssinbattle.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sinbattle.founder_and_clicker()

        # Использование приказа
        self.sfighteruse = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sfighteruse.png', 50,
                                        error_tutorial,
                                        '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sfighteruse.founder_and_clicker()

        # Нажатие на стрелку и скролл вниз
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.arrow_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Выбор стрелков для подкрепа
        time.sleep(5)
        pyautogui.moveTo(371, 348)
        pyautogui.click()
        pyautogui.moveTo(233, 169)
        time.sleep(5)
        pyautogui.click()
        pyautogui.doubleClick()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на кнопку "Хорошо" и скролл вверх
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 300)")

        # Нажатие на иконку миссии со штабом
        self.shq = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\shq.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.shq.founder_and_clicker()

        # Нажатие на кнопку "Приступить" и скролл вниз
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Нажатие на иконку "Магазина"
        self.sstorebutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sstorebutton.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sstorebutton.founder_and_clicker()

        # Нажатие на иконку "Купить"
        self.sbuybutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sbuybutton.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sbuybutton.founder_and_clicker()

        # Нажатие на стрелку 2 стрелку и скролл вверх
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.arrow_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на стрелку 2 стрелку
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.arrow_clicker()

        # Нажатие на кнопку "Plus"
        self.splus = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\splus.png', 50,
                                  error_tutorial,
                                  '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.splus.founder_and_clicker()

        # Выбор штурмовиков в штабе
        time.sleep(10)
        pyautogui.moveTo(212, 326)
        pyautogui.click()

        time.sleep(1)
        pyautogui.moveTo(313, 326)
        pyautogui.click()

        time.sleep(1)
        pyautogui.moveTo(419, 326)
        pyautogui.click()

        time.sleep(1)
        pyautogui.moveTo(533, 326)
        pyautogui.click()

        # Нажатие на кнопку "Хорошо" и скролл вверх
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, 300)")

        # Нажатие на иконку квеста обороны
        self.sdefense = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sdefense.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sdefense.founder_and_clicker()

        # Нажатие на кнопку "Приступить" и скролл вниз
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Нажатие на иконку обороны
        self.sdef = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sdef.png', 50,
                                 error_tutorial,
                                 '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sdef.founder_and_clicker()

        # Нажатие на иконку "Магазина"
        self.sstorebutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sstorebutton.png', 50,
                                         error_tutorial,
                                         '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sstorebutton.founder_and_clicker()

        # Нажатие на иконку "Купить"
        self.sbuybutton = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sbuybutton.png', 50,
                                       error_tutorial,
                                       '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sbuybutton.founder_and_clicker()

        # Скролл вверх и нажатие на стрелку 2
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.sblue2 = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sblue2.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sblue2.arrow_clicker()

        # Выбор стрелков в обороне
        time.sleep(15)
        pyautogui.moveTo(606, 708)
        pyautogui.click()

        # Выставление стрелков в обороне
        time.sleep(7)
        pyautogui.moveTo(474, 400)
        pyautogui.click()

        # Выбор штурмовиков в обороне
        time.sleep(15)
        pyautogui.moveTo(682, 708)
        pyautogui.click()

        # Выставление штурмовиков в обороне
        time.sleep(7)
        pyautogui.moveTo(463, 383)
        pyautogui.click()

        # Нажатие кнопки "Продолжить "
        self.scontinue = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scontinue.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scontinue.founder_and_clicker()

        # Нажатие кнопки "Продолжить "
        self.scontinue = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scontinue.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scontinue.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие на иконку миссии Главштаба
        time.sleep(20)
        pyautogui.moveTo(24, 249)
        pyautogui.click()

        # Нажатие на кнопку "Приступить" и скролл вниз
        self.sproceed = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sproceed.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sproceed.founder_and_clicker()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Клик по штабу
        time.sleep(15)
        pyautogui.moveTo(631, 422)
        pyautogui.click()

        # Нажатие на кнопку "Улучшить"
        self.supgrade = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\supgrade.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.supgrade.founder_and_clicker()

        # Нажатие кнопки "Продолжить "
        self.scontinue = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scontinue.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scontinue.founder_and_clicker()

        # Нажатие на кнопку "Закрытия"
        self.scloseok = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scloseok.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scloseok.founder_and_clicker()

        # Нажатие на кнопку "Хорошо лвлапа"
        self.slvlok = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\slvlok.png', 50,
                                     error_tutorial,
                                     '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.slvlok.founder_and_clicker()

        # Нажатие на кнопку "Хорошо"
        self.sgoods = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\sgoods.png', 50,
                                   error_tutorial,
                                   '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.sgoods.founder_and_clicker()

        # Нажатие кнопки "Продолжить "
        self.scontinue = ImageClicker('C:\Automation\Screens\Total_Front\Total_Front_Tutorial\scontinue.png', 50,
                                      error_tutorial,
                                      '\Automation\Reports\Total_Front\TUTORIAL\Test01_tutorial_bug.png')
        self.scontinue.founder_and_clicker()

if __name__ == "__main__":
    unittest.main()