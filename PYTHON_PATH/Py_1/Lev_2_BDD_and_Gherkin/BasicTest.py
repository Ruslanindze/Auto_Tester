#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys
sys.path.append(r'.\..')
#----------------------
import  unittest, time
import DriverManager as DM
#--------------------------------
class Basic_UniT(unittest.TestCase):
    """–одительский класс дл€ тестов и дочерний дл€ unittest"""
    Browser =  None
    Driver = None
    #---------------
    def setUp(cls):
        cls.Driver = DM.Driver_Manager(cls.Browser).driver
        cls.Driver.get('https://www.yandex.ru')

    def tearDown(cls):
        time.sleep(3)
        cls.Driver.quit()
#--------------------------------