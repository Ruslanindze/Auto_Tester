#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Проверка xss-атаки (запуск стороннего скрипта)
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import unittest
import Security_Testing.BasicTest as BT
import Security_Testing.Str_Const as SC
from unittest_data_provider import data_provider
from selenium.webdriver.common.by import By
#--------------------------------
XSS = ['<script>alert("Attention!");</script>',
       '<script>alert("WTF!");</script>',
       '<script>alert("What I can do anything? Can I smoke?");</script>'
       ]
#--------------------------------
class Test_Xss_P(BT.Basic_UniT):
    pass

def test_generator(xss):
    def test(self):
        self.Driver.get(SC.HOME_PAGE)

        element = self.Driver.find_element(By.CSS_SELECTOR, "iframe.game-frame")
        self.Driver.switch_to.frame(element)

        text_box = self.Driver.find_element(By.CSS_SELECTOR, '#query')
        text_box.send_keys(xss)

        butt = self.Driver.find_element(By.ID, "button")
        butt.click()

        self.assertTrue(self.is_alert_present(), "The alarm is not detected, the xss attack failed")
    # --------------------
    return test
#---------------------------------
if '__main__' == __name__:
    for i, x in enumerate(XSS):
        test_name = 'test_' + str(i)
        test = test_generator(x)
        setattr(Test_Xss_P, test_name, test)
    # ---------------
    unittest.main()