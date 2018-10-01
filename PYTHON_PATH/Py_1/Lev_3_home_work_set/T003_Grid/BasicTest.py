#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import time
import unittest

import T003_Grid.DriverManager as DM
import T003_Grid.PageObjC as Obj
import T003_Grid.Str_Const as SC
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