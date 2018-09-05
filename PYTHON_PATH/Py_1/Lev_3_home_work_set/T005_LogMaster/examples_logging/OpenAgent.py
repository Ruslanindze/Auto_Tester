#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#----------------------------------------------------------------
# � ���� ���� ������ �� ��������, �� ������ ����� �������.
# ��� ���� � ������� *.tlz, ������� ����������� ������
#   TrueLog Explorer, ������� ��� ��� ��������
# ��������: https://community.microfocus.com/borland/test/silk_test/b/weblog/posts/advanced-logging-for-your-selenium-tests-with-python
# ��� ���� ��� ����� TrueLog API ����� import swagger_client, �� �� � ��� ����� �� ��������,
#   ��� ��� ������ swagger_client.DefaultApi() �� ����������...
#----------------------------------------------------------------
PATH_DRIVER_FIREFOX = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\geckodriver.exe"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest, time
#----------------------------------------------------------------
class InsuranceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        capabilities = {"browserName" : "firefox",
                        "silkTestOptions" : {
                            "trueLogPath": '{}.tlz'.format(__file__[:-3]),
                            "trueLogScreenshotMode" : "always"
                        }}

        # � ����� �������� �� ��������, ��� ��������� desired_capabilities �� ��
        # cls.driver = webdriver.Firefox(executable_path=PATH_DRIVER_FIREFOX, desired_capabilities=capabilities)

        # ��� ������ �������� ���������� ��������� hub - node (browser = firefox)
        cls.driver = webdriver.Remote(command_executor='http://172.20.1.150:4444/wd/hub',\
                                      desired_capabilities=capabilities)

    def test_A(self):
        """Testing Google title in driver"""
        # ���� ������ �� ��
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def test_B(self):
        """Testing Yandex title in driver"""
        # ���� ���������� ��������� ��� ������������ ����������� ������� �����������
        self.driver.get("http://www.yandex.ru")
        self.assertEqual(self.driver.title, "�����")

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

# ----------------------------------------
if '__main__' == __name__:
    unittest.main()