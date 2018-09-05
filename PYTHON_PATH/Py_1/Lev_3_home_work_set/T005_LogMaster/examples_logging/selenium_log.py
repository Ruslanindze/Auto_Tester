#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# ������������ ������������� ������ �����������, ��� ��� � ������ �����
# ��� � �������� ��������� � (��������� � �����) ����� �������
# ���� ���� ���� ���������, �� ���������� ���������� ��� ����� ��
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
        # service_log_path - ������ ��������� �������� �������� � ����������
        cls.driver = webdriver.Chrome(executable_path=PATH_DRIVER_CHROME, \
                    service_log_path="selenium_log.log")

        # � capabilities ���� ����� loggingPrefs...
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
        self.assertEqual(self.driver.title, "������")

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

#--------------------------------

if __name__ == '__main__':
    unittest.main()