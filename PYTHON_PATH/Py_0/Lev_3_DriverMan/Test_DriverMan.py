#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys
sys.path.append(r'd:\WORK_MC_21\Tester\Auto_Tester\PYTHON_PATH\Py_0')
#--------------------------------
import unittest
import Lev_3_DriverMan.PageObjC as Obj
import Lev_3_DriverMan.LocatorsC as Loc
import Lev_3_DriverMan.DriverManager as DM
import Lev_3_DriverMan.Str_Const as SC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# ----------------------------------------
class Test_DriverMan(unittest.TestCase):
    browser = None
    Departure = "San Diego"
    #----------------------
    def __asserEq(self, obj_1, obj_2):
        self.assertEqual(obj_1, obj_2)

    @classmethod
    def setUpClass(self):
        self.driver = DM.Driver_Manager(self.browser).driver
        self.HomeP = Obj.Home(self.driver)

    @classmethod
    def tearDownClass(self):
        Obj.time.sleep(3)
        self.driver.quit()

    def test_DepCity(self):
        print('test_DepCity', self.browser)
        check_elem = self.HomeP.departure_city
        select_elem = Select(check_elem)
        select_elem.select_by_visible_text(self.Departure)
        self.__asserEq(check_elem.get_attribute('value'), self.Departure)

# ----------------------------------------
if '__main__' == __name__:
    # unittest.main()

    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)
    RunT = Test_DriverMan
    RunT.browser = 'IE'
    print('tut browser: ', RunT.browser)
    # ----------------------
    result_IE = runner.run(loader.loadTestsFromTestCase(RunT))
    # ----------------------
    RunT.browser = 'firefox'
    result_FF = runner.run(loader.loadTestsFromTestCase(RunT))
