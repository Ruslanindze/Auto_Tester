#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Если использовать сырую библиотеку logging, то смысла я в ней не вижу.
# logging логирует либо просто запросы и то только в режиме DEBUG,
#   либо то, что укажешь сам, типа logging.warning("Происходит что то опасное")
# Однако в сочатании с каким-нибудь другим логером , можно использовать вместо
#   обычного print или перенаправления потока, удобный вывод, если настроить
#   logging.basicConfig()
#--------------------------------
import logging
import unittest, time, os
from selenium import webdriver

PATH_DRIVER_CHROME = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"
#--------------------------------
logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename='logging_example.log'
)
#--------------------------------
class Test_Logging_INFO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=PATH_DRIVER_CHROME)

    def test_A(self):
        """Testing Google title in driver"""
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def test_B(self):
        """Testing Yandex title in driver but with Google parameter"""
        self.driver.get("http://www.yandex.ru")
        self.assertEqual(self.driver.title, "Google")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

#--------------------------------

if __name__ == '__main__':
    unittest.main()