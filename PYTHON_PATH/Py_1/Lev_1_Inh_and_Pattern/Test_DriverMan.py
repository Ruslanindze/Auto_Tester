#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import unittest, json, time
from selenium import webdriver
from selenium.webdriver.support.select import Select
#-----------------------
import BasicTest as BT
import PageObjC as Obj
import LocatorsC as Loc
import DriverManager as DM
import Str_Const as SC
# ----------------------------------------
with open(SC.PATH_JSON) as json_data:
    P = json.load(json_data)
#----------------------------------------
class Test_DriverMan(BT.Basic_UniT):
    Browser = P['Browser']
    #-------------------
    def test_A_City(self):
        check_dep = self.HomeP.departure_city
        select_dep = Select(check_dep)
        check_des = self.HomeP.destination_city
        select_des = Select(check_des)

        select_dep.select_by_visible_text(P['Departure'])
        select_des.select_by_visible_text(P['Destination'])
        self.assertEqual(check_dep.get_attribute('value'),P['Departure'])
        self.assertEqual(check_des.get_attribute('value'), P['Destination'])
    # -----------------
    def test_B_BlueButt(self):
        check_elem = self.HomeP.BlueButton
        # провер€ем, что нажали нужную нам кнопку
        # self.assertEqual(check_elem.get_attribute('value'), "Find Flights")
        self.assertEqual(check_elem.get_attribute('value'), "xxxxx")
        check_elem.click()
        # провер€ем на той ли странице мы оказались
        self.assertEqual(self.driver.current_url, SC.PAGE_CHOOSE)
        # провер€ем по заголовку, те города ли мы выбрали
        # h3 = self.FindFL.H3
        # self.assertIn('from {0} to {1}'.format(P['Departure'], P['Destination']), h3.get_attribute('textContent'))
    # -----------------
    def test_C_ChooseFL(self):
        """ƒанный тест выбирает самую дешевую поездку"""
        Prices = self.Purchase.Prices
        index = -1 # дл€ выборки самой дешевой цены
        price_min = 0 # дл€ выборки самой дешевой цены
        #-----------------------------
        for i, obj in enumerate(Prices):
            price = float(obj.get_attribute('textContent').replace('$', ''))
            if not price_min:
                price_min = price
                index = i
            elif price < price_min:
                price_min = price
                index = i
        # -----------------------------
        Test_DriverMan.Price = price_min
        Chooses = self.FindFL.Chooses
        Chooses[index].click()
        self.assertEqual(self.driver.current_url, SC.PAGE_PURCHASE)
    # -----------------
    # def test_D_Purchase(self):
    #     """“ест провер€ет заголовок и цену, и заполн€ет пол€"""
    #     # ѕровер€ем по заголовку, те ли города мы выбралиы
    #     # h2 = self.Purchase.H2
    #     # self.assertIn('from {0} to {1}'.format(self.Departure, self.Destination), h2.get_attribute('textContent'))
    #
    #     # ѕровер€ем, та ли цена
    #     # Price = self.Purchase.Price
    #     # curr_price = float(Price.get_attribute('textContent').split()[-1])
    #     # self.assertEqual(Price, curr_price)
    #
    #     # --------------------- «аполн€ем формы и делаем проверку
    #     name = self.Purchase.Name
    #     Obj.ImpObj.send_keys(name, P['Name'])
    #     self.assertEqual(P['Name'], name.get_attribute('value'))
    #
    #     address = self.Purchase.Address
    #     Obj.ImpObj.send_keys(address, P['Address'])
    #     self.assertEqual(P['Address'], address.get_attribute('value'))
    #
    #     city = self.Purchase.City
    #     Obj.ImpObj.send_keys(city, P['City'])
    #     self.assertEqual(P['City'], city.get_attribute('value'))
    #
    #     state = self.Purchase.State
    #     Obj.ImpObj.send_keys(state, P['State'])
    #     self.assertEqual(P['State'], state.get_attribute('value'))
    #
    #     zip_code = self.Purchase.ZipCode
    #     Obj.ImpObj.send_keys(zip_code, P['ZipCode'])
    #     self.assertEqual(P['ZipCode'], zip_code.get_attribute('value'))
    #
    #     card_type = self.Purchase.CardType
    #     select_card_type = Select (card_type)
    #     select_card_type.select_by_visible_text(P['CardType'])
    #     self.assertEqual(P['CardType'], select_card_type.first_selected_option.text)
    #
    #     credit_card_numb = self.Purchase.CreditCardNumber
    #     Obj.ImpObj.send_keys(credit_card_numb, P['CredCardNumb'])
    #     self.assertEqual(P['CredCardNumb'], credit_card_numb.get_attribute('value'))
    #
    #     month = self.Purchase.Month
    #     Obj.ImpObj.send_keys(month, P['Month'])
    #     self.assertEqual(P['Month'], month.get_attribute('value'))
    #
    #     year = self.Purchase.Year
    #     Obj.ImpObj.send_keys(year, P['Year'])
    #     self.assertEqual(P['Year'], year.get_attribute('value'))
    #
    #     name_on_card = self.Purchase.NameonCard
    #     Obj.ImpObj.send_keys(name_on_card, P['NameonCard'])
    #     self.assertEqual(P['NameonCard'], name_on_card.get_attribute('value'))
    #
    #     rememberMe = self.Purchase.RememberMe
    #     rememberMe.click()
    #     self.assertTrue(rememberMe.is_selected())
    #
    #     blue_butt = self.Purchase.BlueButton
    #     blue_butt.click()
    #     self.assertEqual(self.driver.current_url, SC.PAGE_CONFIRM)
    #     # --------------------- «аполн€ем формы и делаем проверку

# ----------------------------------------
if '__main__' == __name__:
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(Test_DriverMan))
    # dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    # buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=buf,
    #     title='Test the Report',  # «аголовок отчета
    #     description='Result of tests'  # ќписание отчета
    # )
    # runner.run(suite)

    # pass