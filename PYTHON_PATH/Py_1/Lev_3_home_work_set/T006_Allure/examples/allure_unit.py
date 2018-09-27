# -*- coding: utf-8 -*-

#------------- in windows cmd
#Run: python -m pytest allure_ex_0.py --alluredir ./res_allure_unit
#Show_report: allure serve ./res_allure_unit/
#Gen_report : allure generate -c -o rep_allure_unit res_allure_unit
#Gen_report_2 : allure generate -c -o dir_to dir_from (-c -> clean, -o - by default allure-report)
#------------- in windows cmd

import os, unittest, pytest, allure
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH_CHROME_DR = r'd:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe'

class DemoAllure(unittest.TestCase):

    def test_site_loads(self):
        with pytest.allure.step("Launch site"):
            driver = webdriver.Chrome(executable_path=PATH_CHROME_DR)
            driver.get("http://qaboy.com/")
        with pytest.allure.step("Verify Title loaded"):
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))

class DemoAllure_fix(unittest.TestCase):

    def test_site_loads(self):
        self.launch_site()
        self.verify_site()

    @pytest.allure.step("Launch site")
    def launch_site(self):
        self.driver = webdriver.Chrome(PATH_CHROME_DR)
        self.driver.get("http://qaboy.com/")

    @pytest.allure.step("Verify Title loaded")
    def verify_site(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))

if __name__ == '__main__':
    unittest.main()