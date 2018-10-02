#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#------------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#------------------------------------
import unittest, os, sys
from T002_Jenkins.BasicTest import Basic_UniT as BT
#------------------------------------
class Translate_Ru_En(BT):
    """Тесты проверяющие перевод с русского на английский"""
    #--------------------------------------------
    def test_A(self):
        pass
    # --------------------------------------------