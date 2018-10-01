import unittest, pytest, allure
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


if __name__ == '__main__':
    unittest.main()