#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys
sys.path.append('')
#--------------------------------
import time
import unittest

import DriverManager as DM
import PageObjC as Obj
import Str_Const as SC
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
        time.sleep(1)
        cls.Driver.quit()
#--------------------------------