#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Функции, реализующие шаги теста travelocity
#--------------------------------
import travelocity.Str_Const as SC
import travelocity.LocatorsC as Loc
from selenium.webdriver.common.keys import Keys
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

    return going_to
#--------------------------------
def filling_check_in(driver, data):
    check_in = driver.find_element(*Loc.Common.Check_in)
    check_in.clear()
    check_in.send_keys(data)

    return check_in
#--------------------------------
def filling_check_out(driver, data):
    check_out = driver.find_element(*Loc.Common.Check_out)
    check_out.click()
    check_out.clear()

    for i in range(50):
        check_out.send_keys(Keys.BACK_SPACE)

    check_out.send_keys(data)

    return check_out
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

    need_hotel = hotels[hotelNum]
    need_hotel.click()
#--------------------------------
def reserved_hotel(driver):
    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 10).\
        until(EC.element_to_be_clickable(Loc.Common.Reserve)).click()

    WebDriverWait(driver, 10).\
        until(EC.element_to_be_clickable(Loc.Common.Reserve_recom)).\
            send_keys(Keys.ENTER)
#--------------------------------