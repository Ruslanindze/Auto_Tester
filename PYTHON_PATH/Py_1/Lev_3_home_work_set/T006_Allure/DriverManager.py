#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#----------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
from selenium import webdriver
import T006_Allure.Str_Const as SC
#----------------------

#--------------------------------
class Driver_Manager(object):
    count_run = 0
    def __init__(self, browser = None, options = None):
        Driver_Manager.count_run += 1
        if not getattr(Driver_Manager, "__driver", None):
            if not browser or "chrome" == browser.lower():
                if options:
                    # создадим веб-драйвер с  профилем для browsermobproxy
                    self.__driver = webdriver.Chrome(
                        executable_path=SC.PATH_DRIVER_CHROME,\
                        chrome_options=options)
                else:
                    self.__driver = webdriver.Chrome(
                        executable_path=SC.PATH_DRIVER_CHROME)
            elif 'firefox' == browser.lower():
                if options:
                    self.__driver = webdriver.Firefox(\
                        executable_path=SC.PATH_DRIVER_FIREFOX,\
                        firefox_profile=options
                        )
                else:
                    self.__driver = webdriver.Firefox( \
                        executable_path=SC.PATH_DRIVER_FIREFOX)
            elif "ie" == browser.lower():
                self.__driver = webdriver.Ie(\
                    executable_path=SC.PATH_DRIVER_IE)  # создаем объект, позволяющий запускать сайт в режиме ПО
    # -----------------------------------
    @property
    def driver(self):
        return  self.__driver
    @driver.setter
    def driver(self, new_driver):
        self.__driver = new_driver
# ----------------------------------------------------
# Запуск для отладки
if '__main__' == __name__:
    pass