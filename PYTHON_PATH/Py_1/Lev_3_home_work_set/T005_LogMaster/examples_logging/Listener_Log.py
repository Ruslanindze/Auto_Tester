#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# ���� ������ ����������� ��������� ��� �������� ����������.
# ����� ������������������ ������������� � webdriver ������ _listener
#   ����� EventFiringWebDriver � ������������ �� AbstractEventListener,
#   ��� ����������� ����� ��� ������, ��������������, ������
#   �������� �������� � ������� .png � ������������ � *.log ������ ����������
#   logging.
# ����� � ������ LogListener(AbstractEventListener) ����� �������������� ������
#   � ������ �������������� ������������ (�.: before_click, after_change_value_of � �.�)
# ������ ������ ��� ������ ��� ����� java ->
#   class EventListener implements WebDriverEventListener...
#--------------------------------

PATH_DRIVER_CHROME = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"

import unittest, time, datetime, logging
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener
#------------------------------------------

class LogListener(AbstractEventListener):
    """������ ����� ��������� ��� ������������� � webdriver ������ _listener"""
    def on_exception(self, exception, driver):
        logging.error('#ERROR: {}'.format(exception))
        driver.get_screenshot_as_file('{}.png'.format(__file__[:-3]))

#------------------------------------------
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # �������� ����������� � _listener ��� ����������� ������
        driver = webdriver.Chrome(PATH_DRIVER_CHROME) # �������� �������� ��������
        cls.driver = EventFiringWebDriver(driver, LogListener()) # ����������� �������

        # ��������� logging, ���������, ����� ���� �������� ������� print
        logging.basicConfig(format='%(asctime)s %(message)s', \
                            datefmt='%m/%d/%Y %I:%M:%S %p',\
                            filename= '{}.log'.format(__file__[:-3])) # __file__ - ��� �������

    def test_A(self):
        """Testing Google title in driver"""

        # ���� ������ �� ��
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def test_B(self):
        """Testing Yandex title in driver but with bad parameter"""

        # ���� ���������� ��������� ��� ������������ ����������� ������� �����������
        self.driver.get("http://www.yandex.ru")
        self.assertEqual(self.driver.title, "�����")

    def tearDown(self):
        # ���� � ����� ����� self �� ������ ����� ���������� ����������, ��
        # ��������� ����� on_exception ������� ������ LogListener
        for method, error in self._outcome.errors:
            if error:
                self.driver._listener.on_exception(error, self.driver)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

#----------------------------------------
if '__main__' == __name__:
    unittest.main()