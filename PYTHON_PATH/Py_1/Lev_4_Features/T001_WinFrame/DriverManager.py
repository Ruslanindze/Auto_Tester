#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
from selenium import webdriver
#--------------------------------
PATH_DRIVER_CHROME = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"
PATH_DRIVER_IE = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\IEDriverServer.exe"
PATH_DRIVER_FIREFOX = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\geckodriver.exe"
#------------------------------------------------------------------

#--------------------------------
class Driver_Manager(object):
    count_run = 0
    def __init__(self, browser = ""):
        Driver_Manager.count_run += 1
        if not getattr(Driver_Manager, "__driver", None):
            if not browser or "chrome" == browser.lower():
                self.__driver = webdriver.Chrome(
                    executable_path=PATH_DRIVER_CHROME)
            elif "ie" == browser.lower():
                self.__driver = webdriver.Ie(\
                    executable_path=PATH_DRIVER_IE)
            elif 'firefox' == browser.lower():
                self.__driver = webdriver.Firefox(\
                    executable_path=PATH_DRIVER_FIREFOX)
    # -----------------------------------
    @property
    def driver(self):
        return  self.__driver
    @driver.setter
    def driver(self, new_driver):
        self.__driver = new_driver
# ----------------------------------------------------

if '__main__' == __name__:
    pass