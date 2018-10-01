#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#------------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#------------------------------------
import unittest
from T001_WinFrame.BasicTest import Basic_UniT as BT
#------------------------------------

class Test_TransP(BT):
    def test_A(self):
        """Проверка перевода слов с картинки"""

        # Выбираем картинку со словами для перевода (En -> Ru)
        self.choose_file = self.TranslateP.choose_file
        self.choose_file.click()
#------------------------------------

if '__main__' == __name__:

    unittest.main()