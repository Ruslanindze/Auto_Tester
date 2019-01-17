#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import json, unittest, pytest, allure
import travelocity.BasicTest as BT
import travelocity.Str_Const as SC
import travelocity.Test_Func as TF
import travelocity.LocatorsC as Loc

from allure.constants import AttachmentType
#-------------------------------- cmd allure
#Run: python -m pytest Test_Travelocity.py --alluredir ./res_allure
#Show_report: allure serve ./res_allure/
#Gen_report : allure generate -c -o rep_allure res_allure
#Gen_report_2 : allure generate -c -o dir_to dir_from (-c -> clean, -o - by default allure-report)
#-------------------------------- cmd allure
class Travelocity(BT.Basic_UniT):
    # считываем входные данные из json
    with open(SC.PATH_DATA) as fin:
        data = json.load(fin)
    # -----------------------
    @pytest.allure.step("Проверка корректного открытия сайта")
    def test_step_1(self):
        """Open the home page"""
        TF.open_start_page(self.Driver_Ef)
        self.assertEqual(self.Driver_Ef.current_url, SC.HOME_PAGE)
    # ------------------------
    @pytest.allure.step("Заполняем поле Going to")
    def test_step_2(self):
        """Filling the field Going to"""
        going_to = TF.filling_going_to(self.Driver_Ef, self.data["dest"], self.data["region"])
        self.assertEqual(going_to.get_attribute('value'), self.data["check_Going_to"])
    # ------------------------
    @pytest.allure.step("Заполняем поле даты Check-In")
    def test_step_3(self):
        """Filling of the check-in data"""
        check_in = TF.filling_check_in(self.Driver_Ef, self.data["CheckInData"])
        self.assertEqual(check_in.get_attribute('value'), self.data["CheckInData"])
    # ------------------------
    @pytest.allure.step("Заполняем поле даты Check-Out")
    def test_step_4(self):
        """Filling of the check-out data"""
        check_out = TF.filling_check_out(self.Driver_Ef, self.data["CheckoutData"])
        self.assertEqual(check_out.get_attribute('value'), self.data["CheckoutData"])
    # ------------------------
    @pytest.allure.step("Выбираем отель и резервируем его")
    def test_step_5(self):
        """Choose and reserved a hotel"""
        TF.click_src_butt(self.Driver_Ef)
        TF.choose_hotel(self.Driver_Ef, self.data["hotelNum"])
        TF.reserved_hotel(self.Driver_Ef)

        self.assertTrue(self.Driver_Ef.find_element(*Loc.Check.Finish))
#--------------------------------


#--------------------------------
if __name__ == '__main__':
    Travelocity.Browser = 'chrome'
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(loader.loadTestsFromTestCase(Travelocity))