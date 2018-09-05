#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Демонстрация бесполезности такого логирования, так как в запись файла
# идёт в основном настройки и (насколько я понял) чисто запросы
# даже есди тест завалится, но вебдрайвер отработает все будет ОК
#--------------------------------

PATH_DRIVER_CHROME = "d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"

import logging
import unittest, time, os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# from selenium.webdriver.remote.remote_connection import LOGGER
# LOGGER.setLevel(logging.WARNING)
#--------------------------------

#--------------------------------
class Test_Logging_INFO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # service_log_path - просто описывает действия запросов и параметров
        cls.driver = webdriver.Chrome(executable_path=PATH_DRIVER_CHROME, \
                    service_log_path="selenium_log.log")

        # у capabilities нету ключа loggingPrefs...
        # capabilities = DesiredCapabilities.CHROME
        # capabilities['loggingPrefs'] = {'browser':'ALL'}
        # cls.driver = webdriver.Chrome(executable_path=PATH_DRIVER_CHROME, \
        #                               desired_capabilities=capabilities)

        # cls.log_master = cls.driver.get_log('server')

    def test_A(self):
        """Testing Google title in driver"""
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def test_B(self):
        """Testing Yandex title in driver but with Google parameter"""
        self.driver.get("http://www.yandex.ru")
        self.assertEqual(self.driver.title, "Яндекс")

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

#--------------------------------

if __name__ == '__main__':
    unittest.main()