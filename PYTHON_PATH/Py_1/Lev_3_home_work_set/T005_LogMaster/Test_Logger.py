#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import logging, unittest, time, os
from selenium import webdriver
from selenium.webdriver import  ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import T005_LogMaster.PageObjC as Obj
import T005_LogMaster.LocatorsC as Loc
import T005_LogMaster.DriverManager as DM
import T005_LogMaster.Str_Const as SC
#--------------------------------

#--------------------------------
class Test_Actions(unittest.TestCase):
    Browser = None
    Driver = None
    #-------------
    def setUp(self):
        self.Driver = DM.Driver_Manager(self.Browser).driver
        self.HomeP = Obj.Home(self.Driver)

    def test_A_Women(self):
        #--------- найдем нужный элемент
        check_elem = self.HomeP.Women
        size_old = check_elem.size
        rgba_old = check_elem.value_of_css_property('background-color')
        # --------- навелём на элемент мышкой
        hover = ActionChains(self.Driver).move_to_element(check_elem)
        hover.perform()
        size_cur = check_elem.size
        rgba_cur = check_elem.value_of_css_property('background-color')
        #---------- зона aseert's
        # проверяем одинаковы ли размеры, путём выкидвания одинаковых значений set
        self.assertEqual(len(set(size_old.items()) ^ set(size_cur.items())), 0)
        self.assertEqual('rgba(0, 0, 0, 0)', rgba_old)
        self.assertEqual('rgba(51, 51, 51, 1)', rgba_cur)

    def test_B_TShirts(self):
        #-------- находим нужные элементы
        women = self.HomeP.Women
        t_shirts = self.HomeP.T_shirts

        #-------- проверяем передвижение мышки и смены цвета
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

        #------- проверка клика мыши
        t_shirts.click()
        self.assertEqual(self.Driver.current_url , SC.TSHIRTS_PAGE)

    def tearDown(self):
        time.sleep(4)
        self.Driver.quit()

#--------------------------------
if __name__ == '__main__':
    Test_Actions.Browser = 'firefox'
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(loader.loadTestsFromTestCase(Test_Actions))