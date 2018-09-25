#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import unittest
import Py_0.Lev_2_TestPageObj.PageObj_c as Obj
import Py_0.Lev_2_TestPageObj.locators_c as Loc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#----------------------------------------
class Home_Page_Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.Driver = Obj.Driver_Manager("Chrome").driver
        self.HP = Obj.Home(self.Driver)

    def test_Travel(self):
        check_elem = self.HP.TravelTheWorld
        self.assertEqual(check_elem.get_attribute("text"), "Travel The World")
        check_elem.click()
        self.assertEqual(self.Driver.current_url, Obj.PAGE_HOME)

    def test_home(self):
        check_elem = self.HP.home
        self.assertEqual(check_elem.get_attribute("text"), "home")
        Obj.ImpactObj.click_obj(self.Driver, check_elem)
        self.assertEqual(self.HP.driver.current_url, Obj.PAGE_LOGIN)

    def test_link_picture(self):
        check_elem = self.HP.link_picture
        self.assertEqual(check_elem.get_attribute("text"), \
                         "destination of the week! The Beach!")
        Obj.ImpactObj.click_obj(self.Driver, check_elem)
        self.assertEqual(self.Driver.current_url, Obj.PAGE_PICTURE)

    def test_departure_city(self):
        check_elem = self.HP.departure_city
        select_elem = Select(check_elem)
        select_elem.select_by_visible_text("Portland")
        self.assertEqual(check_elem.get_attribute('value'), "Portland")

    def test_destination_city(self):
        check_elem = self.HP.destination_city
        select_elem = Select(check_elem)
        select_elem.select_by_visible_text("New York")
        self.assertEqual(check_elem.get_attribute('value'), "New York")

    @classmethod
    def tearDownClass(self):
        Obj.time.sleep(3)
        self.Driver.quit()
#----------------------------------------
if '__main__' == __name__:
    unittest.main()