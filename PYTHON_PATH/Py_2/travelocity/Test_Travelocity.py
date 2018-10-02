#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import json, unittest
import travelocity.BasicTest as BT
import travelocity.Str_Const as SC
import  travelocity.Test_Func as TF
#--------------------------------

#--------------------------------
class Travelocity(BT.Basic_UniT):
    # считываем данные из json-файла
    with open(SC.PATH_DATA) as fin:
        data = json.load(fin)
    # -----------------------
    def test_a(self):
        TF.open_start_page(self.Driver)
        TF.filling_going_to(self.Driver, self.data["dest"], self.data["region"])
        TF.filling_check_in(self.Driver, self.data["CheckInData"])
        TF.filling_check_out(self.Driver, self.data["CheckoutData"])
        TF.click_src_butt(self.Driver)

        TF.choose_hotel(self.Driver, self.data["hotelNum"])
        TF.reserved(self.Driver)
#--------------------------------


#--------------------------------
if __name__ == '__main__':
    Travelocity.Browser = 'firefox'
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(loader.loadTestsFromTestCase(Travelocity))