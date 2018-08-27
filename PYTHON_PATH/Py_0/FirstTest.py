#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# ������ ������ ������������� ������ Selenium, WebDriver � ������������ � ������� ��������� unittest (assert...)
# ����� � ������ ������� ������������ ����� FirstTest, ������� ����������� �� �������� unittest.TestCase (��������� ������)
#--------------------------------
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
#----------------------------------------------------
PATH_DRIVER = "d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"
PATH_SITE = "http://blazedemo.com/index.php"
#----------------------------------------------------

class FirstTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=PATH_DRIVER) # ������� ������, ����������� ��������� ���� � ������ ��

    def test_FirstTest(self):
        driver = self.driver
        driver.get(PATH_SITE)
        # ---------- ������� ��������� ������� ������
        depCity = driver.find_element_by_xpath('/html/body/div[3]/form/select[1]/option[3]') # Choose your departure city
        depCity.click() # ������� ��������� ������� �� ����������� ������

        selectDesCity = driver.find_element_by_xpath('/html/body/div[3]/form/select[2]')
        DesCity = Select(selectDesCity) # Choose your destination city
        DesCity.select_by_visible_text("Berlin") # �������� ������� �� ������ �������� "Berlin"
        # DesCity.select_by_index(3) # �������� ����� ������

        findFlightsButton = driver.find_element_by_xpath('/html/body/div[3]/form/div/input')
        findFlightsButton.click()
        # ---------- ������� ��������� ������� ������

        # ---------- ������� �������� assert
        departsTable = driver.find_element(By.CSS_SELECTOR, 'body > div.container > table > thead > tr > th:nth-child(4)')
        arrivesTable = driver.find_element(By.CSS_SELECTOR, 'body > div.container > table > thead > tr > th:nth-child(5)')

        self.assertEqual(departsTable.get_attribute('textContent'), "Departs: Boston")
        self.assertEqual(arrivesTable.get_attribute('textContent'), "Arrives: Berlin")
        # ---------- ������� �������� assert

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

#-----------------------------
if '__main__' == __name__:
    # ��������� ������ ����� unittest, � �����������, ��� ����� main �������� ����������� ������ � ������ FirstTest
    unittest.main()