#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys
sys.path.append(r'd:\WORK_MC_21\Tester\Auto_Tester\PYTHON_PATH\Py_0')
#--------------------------------
import unittest, time, sys, contextlib
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import Lev_3_DriverMan.LocatorsC as Loc
import Lev_3_DriverMan.Str_Const as SC
import Lev_3_DriverMan.DriverManager as DM
#----------------------------------------------------
class ImpactObj(object):
    """����� � �������� �������� �������� ���-����������"""
    @staticmethod
    def click_obj(driver, obj):
        """����� ������� �� �� �������, ��� ����� ������ �������"""
        try:
            obj.click()
        except:
            err = "� ������� {} ����� ������ ��������� ������� ...".format('click_obj()')
            print(err)
            driver.quit()
            raise SystemExit(1)
    #-------------------------------
    @staticmethod
    def dropdown_obj(driver, obj, name_elem):
        """����� �������� �������� �� ������"""
        try:
            select_obj = Select(obj)
        except:
            err = "� ������� {} ����� ������ ��������� ������� ...".format('impact_dropdown_list()')
            print(err)
            driver.quit()
            raise SystemExit(1)
        else:
            list_elements = [opt.text for opt in obj.find_elements(*Loc.Home.Dropdown_List)]
            try:
                select_obj.select_by_visible_text(name_elem)
            except:
                err = "� ������� {} ����� �������, ������������� � ������� � ���������� ������� ...".\
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
            err = "������� {} ���������� �����������, ��������� ���������� ��������...". \
                format('keys_obj()')
            print(err)
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
# ������ ��� �������
if '__main__' == __name__:
    # driver = DM.Driver_Manager("ie").driver
    # HomeP = Home(driver)
    pass