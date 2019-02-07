#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Реализован класс-родитель, для того, чтобы наследовать и писать тесты
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import time, unittest
import Security_Testing.DriverManager as DM
import Security_Testing.Str_Const as SC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#--------------------------------
class Basic_UniT(unittest.TestCase):
    Browser =  None
    Driver = None
    # ---------------------------
    @classmethod
    def setUpClass(cls):
        cls.Driver = DM.Driver_Manager(cls.Browser).driver
    # ---------------------------
    def tearDown(self):
        time.sleep(3)
    # ---------------------------
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.Driver.quit()
    # -----------------------------------
    def is_alert_present(self):
        wait = WebDriverWait(self.Driver, 10)
        alert = wait.until(EC.alert_is_present())

        if (alert):
            alert.accept()
            return True
        else:
            return False
#--------------------------------