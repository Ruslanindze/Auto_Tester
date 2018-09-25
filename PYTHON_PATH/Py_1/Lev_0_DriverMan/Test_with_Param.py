#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Parametrized import *
import PageObjC as Obj
import LocatorsC as Loc
import DriverManager as DM
import Str_Const as SC
# ----------------------------------------
class Test_DriverMan(ParametrizedTestCase):
    Browser = None
    Departure = "San Diego"
    Destination = "London"
    Price =  0
    #--------- ��� ����������� ��� �������
    Name = "Hank"
    Address = "Street 25/17"
    City = "TaganYork"
    State = "California"
    ZipCode = "666"
    CardType = "Diner's Club"
    CreditCardNumber = "1234567890"
    Month = "8"
    Year = "2018"
    NameonCard = "Hank Silver"
    # --------- ��� ����������� ��� �������
    param = None

    @classmethod
    def setUpClass(cls):
        print('setUpClass', cls.param)
        # cls.Browser = cls.param
    #     cls.driver = DM.Driver_Manager(cls.Browser).driver
    #     cls.HomeP = Obj.Home(cls.driver)
    #     cls.FindFL = Obj.Find_Flights(cls.driver)
    #     cls.Purchase = Obj.Purchase(cls.driver)
    # -----------------
    def test_A_City(self):
        print('test_A_City', self.param)
        # check_dep = self.HomeP.departure_city
        # select_dep = Select(check_dep)
        # check_des = self.HomeP.destination_city
        # select_des = Select(check_des)
        #
        # select_dep.select_by_visible_text(self.Departure)
        # select_des.select_by_visible_text(self.Destination)
        # self.assertEqual(check_dep.get_attribute('value'), self.Departure)
        # self.assertEqual(check_des.get_attribute('value'), self.Destination)
    # # -----------------
    # def test_B_BlueButt(self):
    #     check_elem = self.HomeP.BlueButton
    #     # ���������, ��� ������ ������ ��� ������
    #     self.assertEqual(check_elem.get_attribute('value'), "Find Flights")
    #     check_elem.click()
    #     # ��������� �� ��� �� �������� �� ���������
    #     self.assertEqual(self.driver.current_url, SC.PAGE_CHOOSE)
    #     # ��������� �� ���������, �� ������ �� �� �������
    #     h3 = self.FindFL.H3
    #     self.assertIn('from {0} to {1}'.format(self.Departure, self.Destination), h3.get_attribute('textContent'))
    # # -----------------
    # def test_C_ChooseFL(self):
    #     """������ ���� �������� ����� ������� �������"""
    #     Prices = self.FindFL.Prices
    #     index = -1 # ��� ������� ����� ������� ����
    #     price_min = 0 # ��� ������� ����� ������� ����
    #     #-----------------------------
    #     for i, obj in enumerate(Prices):
    #         price = float(obj.get_attribute('textContent').replace('$', ''))
    #         if not price_min:
    #             price_min = price
    #             index = i
    #         elif price < price_min:
    #             price_min = price
    #             index = i
    #     # -----------------------------
    #     Test_DriverMan.Price = price_min
    #     Chooses = self.FindFL.Chooses
    #     Chooses[index].click()
    #     self.assertEqual(self.driver.current_url, SC.PAGE_PURCHASE)
    # # -----------------
    # def test_D_Purchase(self):
    #     print('Browser', self.Browser)
    #     """���� ��������� ��������� � ����, � ��������� ����"""
    #     # ��������� �� ���������, �� �� ������ �� ��������
    #     h2 = self.Purchase.H2
    #     self.assertIn('from {0} to {1}'.format(self.Departure, self.Destination), h2.get_attribute('textContent'))
    #
    #     # ���������, �� �� ����
    #     Price = self.Purchase.Price
    #     curr_price = float(Price.get_attribute('textContent').split()[-1])
    #     self.assertEqual(self.Price, curr_price)
    #
    #     # --------------------- ��������� ����� � ������ ��������
    #     name = self.Purchase.Name
    #     name.clear()
    #     name.send_keys(self.Name)
    #     self.assertEqual(self.Name, name.get_attribute('value'))
    #
    #     address = self.Purchase.Address
    #     address.clear()
    #     address.send_keys(self.Address)
    #     self.assertEqual(self.Address, address.get_attribute('value'))
    #
    #     city = self.Purchase.City
    #     city.clear()
    #     city.send_keys(self.City)
    #     self.assertEqual(self.City, city.get_attribute('value'))
    #
    #     state = self.Purchase.State
    #     state.clear()
    #     state.send_keys(self.State)
    #     self.assertEqual(self.State, state.get_attribute('value'))
    #
    #     zip_code = self.Purchase.ZipCode
    #     zip_code.clear()
    #     zip_code.send_keys(self.ZipCode)
    #     self.assertEqual(self.ZipCode, zip_code.get_attribute('value'))
    #
    #     card_type = self.Purchase.CardType
    #     select_card_type = Select (card_type)
    #     select_card_type.select_by_visible_text(self.CardType)
    #     self.assertEqual(self.CardType, select_card_type.first_selected_option.text)
    #
    #     credit_card_numb = self.Purchase.CreditCardNumber
    #     credit_card_numb.clear()
    #     credit_card_numb.send_keys(self.CreditCardNumber)
    #     self.assertEqual(self.CreditCardNumber, credit_card_numb.get_attribute('value'))
    #
    #     month = self.Purchase.Month
    #     month.clear()
    #     month.send_keys(self.Month)
    #     self.assertEqual(self.Month, month.get_attribute('value'))
    #
    #     year = self.Purchase.Year
    #     year.clear()
    #     year.send_keys(self.Year)
    #     self.assertEqual(self.Year, year.get_attribute('value'))
    #
    #     name_on_card = self.Purchase.NameonCard
    #     name_on_card.clear()
    #     name_on_card.send_keys(self.NameonCard)
    #     self.assertEqual(self.NameonCard, name_on_card.get_attribute('value'))
    #
    #     rememberMe = self.Purchase.RememberMe
    #     rememberMe.click()
    #     self.assertTrue(rememberMe.is_selected())
    #
    #     blue_butt = self.Purchase.BlueButton
    #     blue_butt.click()
    #     self.assertEqual(self.driver.current_url, SC.PAGE_CONFIRM)
    #     # --------------------- ��������� ����� � ������ ��������

    # # -----------------
    # def tearDown(self):
    #     pass
    #     # Obj.time.sleep(1)
    # # -----------------
    # @classmethod
    # def tearDownClass(cls):
    #     Obj.time.sleep(1)
    #     cls.driver.quit()
# ----------------------------------------
if '__main__' == __name__:
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(Test_DriverMan, param="firefox"))
    unittest.TextTestRunner(verbosity=2).run(suite)