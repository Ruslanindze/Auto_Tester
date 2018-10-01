#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#----------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import T003_Grid.Str_Const as SC
#----------------------

#--------------------------------
class Driver_Manager(object):
    count_run = 0
    capabilities = None
    def __init__(self, browser = ""):
        Driver_Manager.count_run += 1

        if not getattr(Driver_Manager, "__driver", None):
            allowed_browsers = ['chrome', 'firefox', 'ie']
            if browser:
                browser = browser.lower()

            if browser == 'ie':
                Driver_Manager.capabilities = DesiredCapabilities.INTERNETEXPLORER
            elif browser in allowed_browsers:
                Driver_Manager.capabilities = {
                    "browserName": browser,
                    "platform": "WINDOWS",
                }
            self.driver = webdriver.Remote(command_executor='http://172.20.1.150:4444/wd/hub', \
                                           desired_capabilities=self.capabilities)
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