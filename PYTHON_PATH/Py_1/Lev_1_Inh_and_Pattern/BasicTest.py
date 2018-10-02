#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import  unittest, time
import DriverManager as DM
import PageObjC as Obj
#--------------------------------
class Basic_UniT(unittest.TestCase):
    """ђодительский класс для тестов и дочерний для unittest"""
    Browser =  None
    #---------------
    def setUp(cls):
        cls.driver = DM.Driver_Manager(cls.Browser).driver
        cls.HomeP = Obj.Home(cls.driver)
        cls.FindFL = Obj.Find_Flights(cls.driver)
        cls.Purchase = Obj.Purchase(cls.driver)

    def tearDown(cls):
        time.sleep(1)
        cls.driver.quit()
#--------------------------------