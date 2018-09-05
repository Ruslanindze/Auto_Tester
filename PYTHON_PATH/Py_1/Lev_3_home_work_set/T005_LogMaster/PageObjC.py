#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import T005_LogMaster.DriverManager as DM
import T005_LogMaster.Str_Const as SC
import T005_LogMaster.LocatorsC as Loc
#------------------------------------

# ----------------------------------------------------
class Home(object):
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    def __init__(self, driver, path_page = SC.HOME_PAGE):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()
    #-------------
    @property
    def Women(self):
        self.check_path_page()
        self.__Women = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(Loc.Home.Women))
        return self.__Women
    # ---------------------------------
    @property
    def Dresses(self):
        self.check_path_page()
        self.__Dresses = self.driver.find_element(*Loc.Home.Dresses)
        return self.__Dresses
    # ---------------------------------
    @property
    def T_shirts(self):
        self.check_path_page()
        self.__T_shirts = self.driver.find_element(*Loc.Home.T_shirts)
        return self.__T_shirts
    # ---------------------------------
    @property
    def Popular(self):
        self.check_path_page()
        self.__Popular = self.driver.find_element(*Loc.Home.Popular)
        return self.__Popular
    # ---------------------------------
    @property
    def Best_sell(self):
        self.check_path_page()
        self.__Best_sell = self.driver.find_element(*Loc.Home.Best_sell)
        return self.__Best_sell
    # ---------------------------------
    def pause(self, time_sleep):
        time.sleep(time_sleep)
    def quit(self, time_sleep = 0):
        if time_sleep > 0:
            time.sleep(time_sleep)
        self.driver.quit()
    # ---------------------------------

# ----------------------------------------------------

# ������ ��� �������
if '__main__' == __name__:
    pass