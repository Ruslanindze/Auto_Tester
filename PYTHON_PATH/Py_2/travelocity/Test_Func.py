#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Скрипт реализует функции, для создания теста
#--------------------------------
import travelocity.Str_Const as SC
import travelocity.LocatorsC as Loc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#--------------------------------
def open_start_page(driver):
    driver.get(SC.HOME_PAGE)
#--------------------------------
def filling_going_to(driver, dest, region):
    going_to = driver.find_element(*Loc.Common.Going_to)
    going_to.click()
    going_to.send_keys('{}, {}'.format(dest, region))
#--------------------------------
def filling_check_in(driver, data):
    driver.find_element(*Loc.Common.Check_in).send_keys(data)
#--------------------------------
def filling_check_out(driver, data):
    check_out = driver.find_element(*Loc.Common.Check_out)
    check_out.click()
    check_out.clear()
    check_out.send_keys(data)
#--------------------------------
def click_src_butt(driver):
    src_butt = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(Loc.Common.Search)
    )
    src_butt.click()
#--------------------------------
def choose_hotel(driver, hotelNum):
    hotels = WebDriverWait(driver, 3).\
    until(EC.presence_of_all_elements_located(Loc.Common.Hotels))

    need_hotel = list(filter(lambda x: x.get_attribute("target") == hotelNum, hotels))[0]
    need_hotel.click()
#--------------------------------
def reserved(driver):
    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 3).\
        until(EC.element_to_be_clickable(Loc.Common.Reserve)).click()

    WebDriverWait(driver, 3).\
        until(EC.element_to_be_clickable(Loc.Common.Reserve_recom)).click()
#--------------------------------