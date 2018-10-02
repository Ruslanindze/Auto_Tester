#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#------------------------------------
# Тут подтягиваются веб-элементы по вызову из объекта класса
#------------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import T001_WinFrame.DriverManager as DM
# ----------------------------------------------------
PAGE_HOME = "https://translate.yandex.ru/ocr"
# ----------------------------------------------------

# ----------------------------------------------------
class TranslateP(object):
    """Веб-элементы на странице переводчика слов с картинок"""
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    def __init__(self, driver, path_page=PAGE_HOME):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()
    # ---------------------------------
    @property
    def choose_file(self):
        self.check_path_page()
        self.__choose_file = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@class="link"]')))
        return self.__choose_file
    # ---------------------------------
    @property
    def open_translateT(self):
        self.check_path_page()
        self.__translateP = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, \
                                '//span[@class="button" and @data-action]')))
        return self.__translateP
    # ---------------------------------
    @staticmethod
    def get_translate(driver):
        translate = driver.find_element(By.XPATH, '//pre[@id="translation"]/span')
        return translate.text
    # ---------------------------------
    @staticmethod
    def get_lang_translate(driver):
        language = driver.find_element(By.ID, 'dstLangButton')
        return language.text
# ----------------------------------------------------

# ----------------------------------------------------
# для отладки
if '__main__' == __name__:
    pass