#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import unittest, time, sys, contextlib
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import LocatorsC as Loc
import Str_Const as SC
import DriverManager as DM
#----------------------------------------------------
class ImpObj(object):
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
    # -------------------------------
    @staticmethod
    def send_keys(obj, msg):
        try:
            obj.clear()
            obj.send_keys(msg)
        except:
            err = "Функция {} отработала некорректно, проверьте подаваемые значения...". \
                format('send_keys()')
            driver.quit()
            raise SystemExit(1)
# ----------------------------------------------------
class Home(object):
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    def __init__(self, driver, path_page = SC.PAGE_HOME):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()
    #-------------
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
    def __init__(self, driver, path_page = SC.PAGE_LOGIN):
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
class Find_Flights(object):
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    #------------------------------------------
    def __init__(self, driver, path_page = SC.PAGE_CHOOSE):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()
    # --------------
    @property
    def H3(self):
        self.check_path_page()
        self.__H3 = self.driver.find_element(*Loc.Find_Flights.H3)
        return self.__H3
    # --------------
    @property
    def Chooses(self):
        self.check_path_page()
        self.__Chooses = self.driver.find_elements(*Loc.Find_Flights.Chooses)
        return self.__Chooses
    # --------------
    @property
    def Prices(self):
        self.check_path_page()
        self.__Prices = self.driver.find_elements(*Loc.Find_Flights.Prices)
        return self.__Prices
# ----------------------------------------------------
class Purchase(object):
    def check_path_page(self):
        if self.path_page != self.driver.current_url:
            self.driver.get(self.path_page)
    #------------------------------------------
    def __init__(self, driver, path_page = SC.PAGE_PURCHASE):
        self.driver = driver
        self.path_page = path_page
        self.check_path_page()
    # --------------
    @property
    def H2(self):
        self.check_path_page()
        self.__H2 = self.driver.find_element(*Loc.Purchase.H2)
        return self.__H2
    # --------------
    @property
    def Prices(self):
        self.check_path_page()
        self.__Prices = self.driver.find_elements(*Loc.Purchase.Price)
        return self.__Prices
    # --------------
    @property
    def Name(self):
        self.check_path_page()
        self.__Name = self.driver.find_element(*Loc.Purchase.Name)
        return self.__Name
    # --------------
    @property
    def Address(self):
        self.check_path_page()
        self.__Address = self.driver.find_element(*Loc.Purchase.Address)
        return self.__Address
    # --------------
    @property
    def City(self):
        self.check_path_page()
        self.__City = self.driver.find_element(*Loc.Purchase.City)
        return self.__City
    # --------------
    @property
    def State(self):
        self.check_path_page()
        self.__State = self.driver.find_element(*Loc.Purchase.State)
        return self.__State
    # --------------
    @property
    def ZipCode(self):
        self.check_path_page()
        self.__ZipCode = self.driver.find_element(*Loc.Purchase.ZipCode)
        return self.__ZipCode
    # --------------
    @property
    def CardType(self):
        self.check_path_page()
        self.__CardType = self.driver.find_element(*Loc.Purchase.CardType)
        return self.__CardType
    # --------------
    @property
    def CreditCardNumber(self):
        self.check_path_page()
        self.__CreditCardNumber = self.driver.find_element(*Loc.Purchase.CreditCardNumber)
        return self.__CreditCardNumber
    # --------------
    @property
    def Month(self):
        self.check_path_page()
        self.__Month = self.driver.find_element(*Loc.Purchase.Month)
        return self.__Month
    # --------------
    @property
    def Year(self):
        self.check_path_page()
        self.__Year = self.driver.find_element(*Loc.Purchase.Year)
        return self.__Year
    # --------------
    @property
    def NameonCard(self):
        self.check_path_page()
        self.__NameonCard = self.driver.find_element(*Loc.Purchase.NameonCard)
        return self.__NameonCard
    # --------------
    @property
    def RememberMe(self):
        self.check_path_page()
        self.__RememberMe = self.driver.find_element(*Loc.Purchase.RememberMe)
        return self.__RememberMe
    # --------------
    @property
    def BlueButton(self):
        self.check_path_page()
        self.__BlueButton = self.driver.find_element(*Loc.Purchase.BlueButton)
        return self.__BlueButton
# ----------------------------------------------------
# Запуск для отладки
if '__main__' == __name__:
    driver = DM.Driver_Manager("ie").driver
    HomeP = Home(driver)
    pass