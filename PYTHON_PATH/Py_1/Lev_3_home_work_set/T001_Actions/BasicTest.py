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

import T001_Actions.DriverManager as DM
import T001_Actions.PageObjC as Obj
import T001_Actions.Str_Const as SC
#--------------------------------

#--------------------------------
class Basic_UniT(unittest.TestCase):
    Browser =  None
    Driver = None
    #---------------
    def setUp(cls):
        cls.Driver = DM.Driver_Manager(cls.Browser).driver
        cls.HomeP = Obj.Home(cls.Driver)

    def tearDown(cls):
        time.sleep(1)
        cls.Driver.quit()
#--------------------------------