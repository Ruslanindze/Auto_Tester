#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#----------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
from selenium import webdriver
import T005_LogMaster.Str_Const as SC
#----------------------

#--------------------------------
class Driver_Manager(object):
    count_run = 0
    def __init__(self, browser = ""):
        Driver_Manager.count_run += 1
        if not getattr(Driver_Manager, "__driver", None):
            if not browser or "chrome" == browser.lower():
                self.__driver = webdriver.Chrome(
                    executable_path=SC.PATH_DRIVER_CHROME)  # ������� ������, ����������� ��������� ���� � ������ ��
            elif "ie" == browser.lower():
                self.__driver = webdriver.Ie(\
                    executable_path=SC.PATH_DRIVER_IE)  # ������� ������, ����������� ��������� ���� � ������ ��
            elif 'firefox' == browser.lower():
                self.__driver = webdriver.Firefox(\
                    executable_path=SC.PATH_DRIVER_FIREFOX, \
                    service_log_path=SC.PATH_LOG)  # ������� ������, ����������� ��������� ���� � ������ ��
    # -----------------------------------
    @property
    def driver(self):
        return  self.__driver
    @driver.setter
    def driver(self, new_driver):
        self.__driver = new_driver
# ----------------------------------------------------
# ������ ��� �������
if '__main__' == __name__:
    pass