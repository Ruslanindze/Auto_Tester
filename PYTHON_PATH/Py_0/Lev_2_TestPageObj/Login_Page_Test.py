#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import unittest
import Py_0.Lev_2_TestPageObj.PageObj_c as Obj
import Py_0.Lev_2_TestPageObj.locators_c as Loc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#----------------------------------------
class Login_Page_Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        driverMan = Obj.Driver_Manager('Chrome')
        self.Driver = driverMan.driver
        self.LP = Obj.Login(self.Driver)

    def test_Blaze(self):
        check_elem = self.LP.BlazeDemo
        self.assertEqual(check_elem.get_attribute("class"), "navbar-brand")
        check_elem.click()
        self.assertEqual(self.Driver.current_url, Obj.PAGE_HOME_Not_php)

    def test_LogUp(self):
        check_elem = self.LP.LoginUp
        self.assertEqual(check_elem.get_attribute("text"), "Login")

    def test_RegUp(self):
        check_elem = self.LP.RegisterUp
        self.assertEqual(check_elem.get_attribute("text"), "Register")
        check_elem.click()
        self.assertEqual(self.Driver.current_url, Obj.PAGE_REGIS)

    def test_Email(self):
        check_elem = self.LP.Email
        self.assertEqual(check_elem.get_attribute("id"), "email")
        check_elem.send_keys("route666@mail.ru")
        self.assertEqual(check_elem.get_attribute('value'), "route666@mail.ru")

    def test_Pass(self):
        check_elem = self.LP.Password
        self.assertEqual(check_elem.get_attribute("id"), "password")
        check_elem.send_keys("666")
        self.assertEqual(check_elem.get_attribute('value'), "666")

    def test_Remember(self):
        check_elem = self.LP.RememberMe
        self.assertEqual(check_elem.get_attribute("name"), "remember")
        check_elem.click()

    def test_Forgot(self):
        check_elem = self.LP.ForgotPassword
        self.assertEqual(check_elem.get_attribute("class"), "btn btn-link")
        check_elem.click()
        self.assertEqual(self.Driver.current_url, Obj.PAGE_FORGOT_PASS)

    @classmethod
    def tearDownClass(self):
        Obj.time.sleep(5)
        self.Driver.quit()
#----------------------------------------
if '__main__' == __name__:
    unittest.main()