#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import unittest, time, os
from selenium import webdriver
from selenium.webdriver import  ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner

import T001_Actions.BasicTest as BT
import T001_Actions.PageObjC as Obj
import T001_Actions.LocatorsC as Loc
import T001_Actions.DriverManager as DM
import T001_Actions.Str_Const as SC
#--------------------------------

#--------------------------------
class Test_Actions(BT.Basic_UniT):
    Browser = None
    #-------------------
    def test_A_Women(self):
        """Проверка изменения цвета при наведении мышки на WOMEN"""

        check_elem = self.HomeP.Women
        size_old = check_elem.size
        rgba_old = check_elem.value_of_css_property('background-color')

        hover = ActionChains(self.Driver).move_to_element(check_elem)
        hover.perform()
        size_cur = check_elem.size
        rgba_cur = check_elem.value_of_css_property('background-color')

        self.assertEqual(len(set(size_old.items()) ^ set(size_cur.items())), 0)
        self.assertEqual('rgba(0, 0, 0, 0)', rgba_old)
        self.assertEqual('rgba(51, 51, 51, 1)', rgba_cur)

    def test_B_TShirts(self):
        """Проверка изменения цвета при наведении мышки на TShirts"""

        women = self.HomeP.Women
        t_shirts = self.HomeP.T_shirts

        rgba_women_0 = women.value_of_css_property('background-color')
        self.assertEqual('rgba(0, 0, 0, 0)', rgba_women_0)
        rgba_t_shirts_0 = t_shirts.value_of_css_property('background-color')
        self.assertEqual('rgba(0, 0, 0, 0)', rgba_t_shirts_0)

        ActionChains(self.Driver).move_to_element(women).perform()
        rgba_women_1 = women.value_of_css_property('background-color')
        self.assertEqual('rgba(51, 51, 51, 1)', rgba_women_1)
        ActionChains(self.Driver).move_to_element(t_shirts).perform()
        rgba_t_shirts_1 = t_shirts.value_of_css_property('background-color')
        self.assertEqual('rgba(51, 51, 51, 1)', rgba_t_shirts_1)

        t_shirts.click()
        self.assertEqual(self.Driver.current_url , SC.TSHIRTS_PAGE)

#--------------------------------
if __name__ == '__main__':
    output = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                          "{}".format('Reports'))
    unittest.main(
        testRunner=HTMLTestRunner(verbosity=2, output=output, report_name='Report2_{}'\
                                  .format(time.strftime("%H%M%S", time.localtime())),
                                  report_title='Report_2', failfast=False))