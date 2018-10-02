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

import T002_Jenkins.DriverManager as DM
import T002_Jenkins.LocatorC as LC
import T002_Jenkins.Str_Const as SC
# ----------------------------------------------------
class TranslateT(object):
    """Объекты яндекс-переводчика раздела ТЕКСТ"""
    #--------------------------------------------
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    # --------------------------------------------
    def __init__(self, driver, path_page=SC.PAGE_TEXT):
        self.driver = driver
        self.path_page = path_page
    # --------------------------------------------
    @property
    def left_pane_tr(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Text.left_pane_tr)
    #--------------------------------------------
    @property
    def left_pane_lang(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Text.left_pane_lang)
    # --------------------------------------------
    @property
    def right_pane_tr(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Text.right_pane_tr)
    # --------------------------------------------
    @property
    def right_pane_lang(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Text.right_pane_lang)
    # --------------------------------------------
    @property
    def switch_dir(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Text.switch_dir)
    # --------------------------------------------

# ----------------------------------------------------
class TranslateS(object):
    """Объекты яндекс-переводчика раздела САЙТ"""
    #--------------------------------------------
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    def __init__(self, driver, path_page=SC.PAGE_PICT):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()
    # --------------------------------------------
    @property
    def original(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Site.original)
    # --------------------------------------------
    @property
    def translation(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Site.translation)
    # --------------------------------------------
    @property
    def input_site(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Site.input_site)
    # --------------------------------------------
    @property
    def translate(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Site.translate)
    # --------------------------------------------

# ----------------------------------------------------
class TranslateP(object):
    """Объекты яндекс-переводчика раздела КАРТИНКА"""
    #--------------------------------------------
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    def __init__(self, driver, path_page=SC.PAGE_PICT):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()
    # ---------------------------------
    @property
    def choose_file(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Picture.choose_file)
    # ---------------------------------
    @property
    def from_lang(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Picture.from_lang)
    # ---------------------------------
    @property
    def to_lang(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Picture.to_lang)
    # ---------------------------------
    @property
    def open_translateT(self):
        self.check_path_page()
        return self.driver.find_element(*LC.Picture.open_in_tr)
    # ---------------------------------

# ----------------------------------------------------

if '__main__' == __name__:
    pass