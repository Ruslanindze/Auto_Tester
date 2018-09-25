#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import unittest, time, sys, contextlib
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import Py_0.Lev_2_TestPageObj.locators_c as Loc
#----------------------------------------------------
PATH_DRIVER_CHROME = "d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"
PAGE_HOME = "http://www.blazedemo.com/index.php"
PAGE_HOME_Not_php = "http://www.blazedemo.com/"
PAGE_PICTURE = "http://www.blazedemo.com/vacation.html"
PAGE_LOGIN = 'http://www.blazedemo.com/login'
PAGE_REGIS = 'http://www.blazedemo.com/register'
PAGE_FORGOT_PASS = 'http://www.blazedemo.com/password/reset'
PAGE_CHOOSE = 'http://www.blazedemo.com/reserve.php'
PAGE_PURCHASE = 'http://www.blazedemo.com/purchase.php'
#----------------------------------------------------
class Driver_Manager(object):
    count_run = -1
    def __init__(self, browser):
        Driver_Manager.count_run += 1
        # if Driver_Manager.count_run == 0:
        if "Chrome" == browser:
            self.__driver = webdriver.Chrome(
                executable_path=PATH_DRIVER_CHROME)  # создаем объект, позволяющий запускать сайт в режиме ПО
    # -----------------------------------
    @property
    def driver(self):
        return  self.__driver
    @driver.setter
    def driver(self, new_driver):
        self.__driver = new_driver
# ----------------------------------------------------
class ImpactObj(object):
    """Класс с методами проверки основных веб-эелементов"""
    @staticmethod
    def click_obj(driver, obj):
        """Метод кликает на те объекты, где можно только кликать"""
        try:
            obj.click()
        except:
            err = "В функцию {} подан объект неверного формата ...".format('click_obj()')
            print(err)
            driver.quit()
            raise SystemExit(1)
    #-------------------------------
    @staticmethod
    def dropdown_obj(driver, obj, name_elem):
        """Метод выбирает эедемент из списка"""
        try:
            select_obj = Select(obj)
        except:
            err = "В функцию {} подан объект неверного формата ...".format('impact_dropdown_list()')
            print(err)
            driver.quit()
            raise SystemExit(1)
        else:
            list_elements = [opt.text for opt in obj.find_elements(*Loc.Home.Dropdown_List)]
            try:
                select_obj.select_by_visible_text(name_elem)
            except:
                err = "В функцию {} подан елемент, отсутствующий в объекте с выпадающим списком ...".\
                    format('impact_dropdown_list()')
                print(err)
                driver.quit()
                raise SystemExit(1)
    # -------------------------------
    @staticmethod
    def keys_obj(driver, obj, send_keys):
        try:
            obj.send_keys(send_keys)
        except:
            err = "Функция {} отработала некорректно, проверьте подаваемые значения...". \
                format('keys_obj()')
            print(err)
            driver.quit()
            raise SystemExit(1)
# ----------------------------------------------------
class Home(object):
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    def __init__(self, driver, path_page = PAGE_HOME):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()

    @property
    def TravelTheWorld(self):
        self.check_path_page()
        self.__TravelTheWorld = self.driver.find_element(*Loc.Home.TravelTheWorld)
        return self.__TravelTheWorld
    #--------------
    @property
    def home(self):
        self.check_path_page()
        self.__home = self.driver.find_element(*Loc.Home.home)
        return self.__home
    # --------------
    @property
    def link_picture(self):
        self.check_path_page()
        self.__link_picture = self.driver.find_element(*Loc.Home.link_picture)
        return self.__link_picture
    # --------------
    @property
    def departure_city(self):
        self.check_path_page()
        self.__departure_city = self.driver.find_element(*Loc.Home.departure_city)
        return self.__departure_city
    # --------------
    @property
    def destination_city(self):
        self.check_path_page()
        self.__destination_city = self.driver.find_element(*Loc.Home.destination_city)
        return self.__destination_city
    # --------------
    @property
    def BlueButton(self):
        self.check_path_page()
        self.__BlueButton = self.driver.find_element(*Loc.Home.BlueButton)
        return self.__BlueButton
        # --------------
    # ---------------------------------
    def pause(self, time_sleep):
        time.sleep(time_sleep)
    def quit(self, time_sleep = 0):
        if time_sleep > 0:
            time.sleep(time_sleep)
        self.driver.quit()
    # ---------------------------------
# ----------------------------------------------------
class Login(object):
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    #------------------------------------------
    def __init__(self, driver, path_page = PAGE_LOGIN):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()

    @property
    def BlazeDemo(self):
        self.check_path_page()
        self.__BlazeDemo = self.driver.find_element(*Loc.Login.BlazeDemo)
        return self.__BlazeDemo
    # --------------
    @property
    def LoginUp(self):
        self.check_path_page()
        self.__LoginUp = self.driver.find_element(*Loc.Login.LoginUp)
        return self.__LoginUp
    # --------------
    @property
    def RegisterUp(self):
        self.check_path_page()
        self.__RegisterUp = self.driver.find_element(*Loc.Login.RegisterUp)
        return self.__RegisterUp
    # --------------
    @property
    def Email(self):
        self.check_path_page()
        self.__Email = self.driver.find_element(*Loc.Login.Email)
        return self.__Email
    # --------------
    @property
    def Password(self):
        self.check_path_page()
        self.__Password = self.driver.find_element(*Loc.Login.Password)
        return self.__Password
    # --------------
    @property
    def RememberMe(self):
        self.check_path_page()
        self.__RememberMe = self.driver.find_element(*Loc.Login.RememberMe)
        return self.__RememberMe
    # --------------
    @property
    def BlueButton(self):
        self.check_path_page()
        self.__BlueButton = self.driver.find_element(*Loc.Login.BlueButton)
        return self.__BlueButton
    # --------------
    @property
    def ForgotPassword(self):
        self.check_path_page()
        self.__ForgotPassword = self.driver.find_element(*Loc.Login.ForgotPassword)
        return self.__ForgotPassword
    # ---------------------------------
    def pause(self, time_sleep):
        time.sleep(time_sleep)
    def quit(self, time_sleep = 0):
        if time_sleep > 0:
            time.sleep(time_sleep)
        self.driver.quit()
    # ---------------------------------
# ----------------------------------------------------
if '__main__' == __name__:
    # driverMan = Driver_Manager('Chrome') # запускаем драйвер, причем только один раз
    # driver = driverMan.driver

    # -------- проверка Home Page
    # home = Home(driver)
    # ImpactObj.click_obj(home.driver, home.home)
    # home.pause(3)
    #
    # ImpactObj.click_obj(home.driver, home.TravelTheWorld)
    # home.pause(3)
    #
    # ImpactObj.dropdown_obj(home.driver, home.departure_city, "Portland")
    # home.pause(3)
    #
    # ImpactObj.dropdown_obj(home.driver, home.destination_city, "Dublin")
    # home.pause(3)
    #
    # ImpactObj.click_obj(home.driver, home.BlueButton)
    # home.quit(3)
    # -------- проверка Home Page

    # ---------- проверка Login Page
    # log_page = Login(driver)
    # log_page.pause(2)
    #
    # ImpactObj.click_obj(log_page.driver, log_page.BlazeDemo)
    # log_page.pause(2)
    #
    # ImpactObj.click_obj(log_page.driver, log_page.RegisterUp)
    # log_page.pause(2)
    #
    # ImpactObj.click_obj(log_page.driver, log_page.LoginUp)
    # log_page.pause(2)
    #
    # ImpactObj.click_obj(log_page.driver, log_page.RememberMe)
    # ImpactObj.keys_obj(log_page.driver, log_page.Email, "route666@mail.ru")
    # ImpactObj.keys_obj(log_page.driver, log_page.Password, "666")
    #
    # log_page.quit(5)
    # ---------- проверка Login Page
    pass
