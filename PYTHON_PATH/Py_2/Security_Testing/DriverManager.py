#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Скрипт является менеджером драйверов, возвращает веб-драйвер указанного браузера
#--------------------------------
from selenium import webdriver
import Security_Testing.Str_Const as SC
#--------------------------------
class Driver_Manager(object):
    count_run = -1
    def __init__(self, browser = ""):
        Driver_Manager.count_run += 1
        if not getattr(Driver_Manager, "__driver", None):
            if not browser or "chrome" == browser.lower():
                self.__driver = webdriver.Chrome(
                    executable_path=SC.PATH_DRIVER_CHROME)
            elif "ie" == browser.lower():
                self.__driver = webdriver.Ie(\
                    executable_path=SC.PATH_DRIVER_IE)
            elif 'firefox' == browser.lower():
                self.__driver = webdriver.Firefox(\
                    executable_path=SC.PATH_DRIVER_FIREFOX)
    # -----------------------------------
    @property
    def driver(self):
        return  self.__driver
    @driver.setter
    def driver(self, new_driver):
        self.__driver = new_driver

    # -----------------------------------
# ----------------------------------------------------
# для отладки
if '__main__' == __name__:
    pass