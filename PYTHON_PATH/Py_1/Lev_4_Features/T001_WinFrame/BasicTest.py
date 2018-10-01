#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Скрипт с базовым классом, наследуясь от которого можно писать сразу тесты
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import time
import unittest

import T001_WinFrame.DriverManager as DM
import T001_WinFrame.PageObjC as Obj
#--------------------------------

#--------------------------------
class Basic_UniT(unittest.TestCase):
    Browser =  None
    #---------------
    @classmethod
    def setUpClass(cls):
        cls.driver = DM.Driver_Manager(cls.Browser).driver
        cls.TranslateP = Obj.TranslateP(cls.driver)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()
#--------------------------------