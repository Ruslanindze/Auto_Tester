#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import Py_0.Two_Page_Obj as PO

class BasePageElement(object):
    """Base page class that is initialized on every page object class."""
    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.ID, obj.locator))
        driver.find_element(By.ID, obj.locator()).clear()
        driver.find_element(By.ID, obj.locator()).send_keys(value)
    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")

#-----------------------------
if '__main__' == __name__:
    obj = PO.Page_Login(PO.PATH_DRIVER, PO.PATH_PAGE_LOGIN)
    obj.locator = 'email'

    base_elem = BasePageElement()
    base_elem.__set__(obj, 100)

    obj.sleep(7)
    obj.close()