#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
#----------------------------------------------------
PATH_DRIVER = "d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"
PATH_SITE = "http://blazedemo.com/index.php"
PATH_PAGE_LOGIN = 'http://www.blazedemo.com/login'
PATH_PAGE_REGIS = 'http://www.blazedemo.com/register'
PAGE_FORGOT_PASS = 'http://www.blazedemo.com/password/reset'
#----------------------------------------------------
class Page_One:
    """Класс основной страницы, то есть домашней"""
    def __init__(self, path_driver, path_site):
        """При инициализации находим основные контейнеры страниц"""
        #------------------------
        self.driver = webdriver.Chrome(executable_path=path_driver)
        self.path_site = path_site
        self.driver.get(self.path_site)
        # ------------------------
        xPAth_headC = '//div[a="Travel The World"]'
        self.head_cont = self.driver.find_element_by_xpath(xPAth_headC)
        # ------------------------
        xPath_statiC_0 = './/div[h1="Welcome to the Simple Travel Agency!"]'
        self.static_cont_0 = self.driver.find_element_by_xpath(xPath_statiC_0)
        # ------------------------
        xPath_from = '//select[@name = "fromPort"]/option'
        self.departure_city = self.driver.find_elements_by_xpath(xPath_from)
        # ------------------------
        xPath_to = '//select[@name = "toPort"]/option'
        self.destination_city = self.driver.find_elements_by_xpath(xPath_to)
        # ------------------------
        xPath_Find = '//input[@value="Find Flights"]'
        self.find_flights = self.driver.find_element_by_xpath(xPath_Find)
    # --------------------------------
    def get_url_page_home(self):
        xPath_home = '//a[text()="home"]'
        button_home = self.driver.find_element_by_xpath(xPath_home)
        button_home.click()
        #-------
        return self.driver.current_url
    # --------------------------------
    def get_url_beach(self):
        xPath_home = '//a[text()="destination of the week! The Beach!"]'
        button_bitch = self.driver.find_element_by_xpath(xPath_home)
        button_bitch.click()
        #-------------------
        return self.driver.current_url
    # --------------------------------
    def return_home(self):
        self.driver.get(self.path_site)
    def sleep(self,x):
        time.sleep(x)
    def close(self):
        self.driver.quit()
#----------------------------------------------------
class Page_Login:
    """Класс, описывающий страницу переехода по кнопке home"""
    def __init__(self, path_driver, path_page):
        #------------------------
        self.driver = webdriver.Chrome(executable_path=path_driver)
        self.path_page = path_page
        self.driver.get(self.path_page)
        # ------------------------
        selec_BlazeDemo = 'div > div.navbar-header > a'
        self.BlazeDemo = self.driver.find_element_by_css_selector(selec_BlazeDemo)
        # ------------------------
        selec_Login = '#app-navbar-collapse > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a'
        self.Login = self.driver.find_element_by_css_selector(selec_Login)
        # ------------------------
        selec_Register = '#app-navbar-collapse > ul.nav.navbar-nav.navbar-right > li:nth-child(2) > a'
        self.Register = self.driver.find_element_by_css_selector(selec_Register)
        # ------------------------
        self.Mail = self.driver.find_element(By.ID, "email")
        self.Pass = self.driver.find_element(By.ID, "password")
        self.RememberMe = self.driver.find_element(By.NAME, "remember")
        self.ButLogin = self.driver.find_element_by_xpath('//button[@class="btn btn-primary"]')
        self.ForgotPass = self.driver.find_element_by_xpath('//a[@class="btn btn-link"]')
        # ------------------------
    # ------------------------
    def fill_defaults(self):
        self.Mail.send_keys('route_666@mail.ru')
        self.Pass.send_keys("666")
        self.RememberMe.click()

    def return_home(self):
        self.driver.get(self.path_page)
    def sleep(self,x):
        time.sleep(x)
    def close(self):
        self.driver.quit()
#----------------------------------------------------
class Page_Register:
    """Класс, описывающий страницу переехода по кнопке Register"""
    def __init__(self, path_driver, path_page):
        #------------------------
        self.driver = webdriver.Chrome(executable_path=path_driver)
        self.path_page = path_page
        self.driver.get(self.path_page)
        # ------------------------
        selec_BlazeDemo = 'div > div.navbar-header > a'
        self.BlazeDemo = self.driver.find_element_by_css_selector(selec_BlazeDemo)
        # ------------------------
        selec_Login = '#app-navbar-collapse > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a'
        self.Login = self.driver.find_element_by_css_selector(selec_Login)
        # ------------------------
        selec_Register = '#app-navbar-collapse > ul.nav.navbar-nav.navbar-right > li:nth-child(2) > a'
        self.Register = self.driver.find_element_by_css_selector(selec_Register)
        # ------------------------
        self.Name = self.driver.find_element(By.ID, "name")
        self.Company = self.driver.find_element(By.ID, "company")
        self.Mail = self.driver.find_element(By.ID, "email")
        self.Password = self.driver.find_element(By.ID, "password")
        self.Confirm_Password = self.driver.find_element(By.ID, "password-confirm")
        self.ButtReg = self.driver.find_element(By.XPATH, '//button[@class = "btn btn-primary"]')
    #-----------------------
    def fill_defaults(self):
        self.Name.send_keys('John')
        self.Company.send_keys('Red Hot Chili Peppers')
        self.Mail.send_keys('route_666@mail.ru')
        self.Password.send_keys('666')
        self.Confirm_Password.send_keys('666')
        # self.ButtReg.click()

    def return_home(self):
        self.driver.get(self.path_page)
    def sleep(self,x):
        time.sleep(x)
    def close(self):
        self.driver.quit()
# ----------------------------------------------------
class ForgotPass:
    def __init__(self, path_driver, path_page):
        #------------------------
        self.driver = webdriver.Chrome(executable_path=path_driver)
        self.path_page = path_page
        # ------------------------
        self.driver.get(self.path_page)
        selec_BlazeDemo = 'div > div.navbar-header > a'
        self.BlazeDemo = self.driver.find_element_by_css_selector(selec_BlazeDemo)
        # ------------------------
        selec_Login = 'ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a'
        self.Login = self.driver.find_element_by_css_selector(selec_Login)
        # ------------------------
        selec_Register = 'ul.nav.navbar-nav.navbar-right > li:nth-child(2) > a'
        self.Register = self.driver.find_element_by_css_selector(selec_Register)
        # ------------------------
        self.Mail = self.driver.find_element(By.ID, "email")
        self.ButtSendPass = self.driver.find_element(By.XPATH, '//button[@class = "btn btn-primary"]')
        #-------------------------
    def return_home(self):
        self.driver.get(self.path_page)
    def sleep(self,x):
        time.sleep(x)
    def close(self):
        self.driver.quit()
# ----------------------------------------------------
class TableFind:
    pass
# --------------------------------
if '__main__' == __name__:
    # ------------ участок создания класса - Home
    page_one = Page_One(PATH_DRIVER, PATH_SITE)

    print(type(page_one.destination_city))
    page_one.destination_city.select_by_visible_text("London").click()
    # DesCity.select_by_index(3) # Выбираем через индекс

    page_one.sleep(7)
    page_one.close()
    # ------------ участок создания класса - Home

    # #------------ участок создания класса - Login
    # page_home = Page_Login(PATH_DRIVER, PATH_PAGE_LOGIN)

    # page_home.fill_defaults()

    # page_home.sleep(7)
    # page_home.close()
    # # ------------ участок создания класса - Login

    # # ------------ участок создания класса - Register
    # page_register = Page_Register(PATH_DRIVER, PATH_PAGE_REGIS)
    #
    # page_register.fill_defaults()
    #
    # page_register.sleep(5)
    # page_register.close()
    # # ------------ участок создания класса - Register

    # ------------ участок создания класса - ForgotPass
    # forgotPass_page = ForgotPass(PATH_DRIVER, PAGE_FORGOT_PASS)
    # forgotPass_page.Mail.send_keys('fuck the policy!')
    # forgotPass_page.sleep(5)
    # forgotPass_page.close()
    # ------------ участок создания класса - ForgotPass