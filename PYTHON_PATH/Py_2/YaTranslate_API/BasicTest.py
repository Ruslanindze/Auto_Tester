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
#--------------------------------

#--------------------------------
class Basic_UniT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Implementation of the setUpClasss() ...")
    # ---------------------------
    def setUp(self):
        print("\n------- begin_case -------\n")
    # ---------------------------
    def tearDown(self):
        print("\n------- end_case -------\n")
    # ---------------------------
    @classmethod
    def tearDownClass(cls):
        print("Implementation of the tearDownClass() ...")
#--------------------------------