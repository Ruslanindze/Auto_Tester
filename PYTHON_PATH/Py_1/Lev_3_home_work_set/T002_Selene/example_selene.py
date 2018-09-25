#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------
PATH_SITE = r'https://www.artlebedev.ru/'
PATH_DRIVER =  r'd:\WORK_MC_21\Tester\Auto_Tester\chromedriver.exe'
#--------------------
import time
from selenium import webdriver
from selene.api import *
from webdriver_manager.chrome import ChromeDriverManager
from selene.support.jquery_style_selectors import s
#--------------------
def lev_0():
    # browser.open_url(PATH_SITE) # не запускает почему-то
    browser.set_driver(webdriver.Chrome(PATH_DRIVER))

    browser.open_url(PATH_SITE)
    s("#new-todo").set("a").press_enter()
    # s("#new-todo").set("b").press_enter()

    # s("#new-todo").should(be.blank)
    # s("#new-todo").set_value(1).press_enter()
    # ss("#todo-list>li").should(have.exact_texts("1"))

    time.sleep(5)
    browser.quit()
#-------------------------------------------
def lev_1():
    # config.browser_name = "chrome" # один из способов запуска драйвера
    driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.set_driver(driver)
    browser.open_url('http://www.blazedemo.com/purchase.php')

    s("#inputName").set("Ruslan")
    s("#address").set("Ad, 7/1 krug")
    s("#city").set("TaganYork")
    s(by.xpath("/html/body/div[2]/form/div[11]/div/label")).click()
    s("body > div.container > form > div:nth-child(12) > div > input").click()

    time.sleep(7)
    # browser.quit()
#-------------------------------------------
def lev_2():
    class LoginPage(object):
        def __init__(self):
            self.name = s("#inputName")
            self.address = s("#address")
            self.city = s("#city")
            self.remeber  = s(by.xpath("/html/body/div[2]/form/div[11]/div/label"))
            self.button = s("body > div.container > form > div:nth-child(12) > div > input")

        def login_as(self, name, address, city):
            self.name.set(name)
            self.address.set(address)
            self.city.set(city)
            self.remeber.click()
            self.button.click()
    #----------------------
    def test_user_can_name():
        user = ('John', 'Ad, 7/10 cicrle', 'TaganYorkia')
        LoginPage.login_as(user)
    # ----------------------
    # class MainPage(object):
    #     def __init__(self):
    #         self.logo = s()

#-------------------------------------------
if '__main__' == __name__:
    # lev_0()
    lev_1()

    pass