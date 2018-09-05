#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import time
import unittest

import T005_LogMaster.DriverManager as DM
import T005_LogMaster.PageObjC as Obj
import T005_LogMaster.Str_Const as SC
#--------------------------------

#--------------------------------
class Basic_UniT(unittest.TestCase):
    """Родительский класс для тестов и дочерний для unittest"""
    Browser =  None
    Driver = None
    #---------------
    def setUp(cls):
        cls.Driver = DM.Driver_Manager(cls.Browser).driver
        cls.HomeP = Obj.Home(cls.Driver)

    def tearDown(cls):
        time.sleep(4)
        cls.Driver.quit()
#--------------------------------