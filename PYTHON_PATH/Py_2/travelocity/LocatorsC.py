#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
from selenium.webdriver.common.by import By
#--------------------------------
class Common:
    Going_to = (By.XPATH, '//*[@id="hotel-destination-hp-hotel"]')
    Check_in = (By.XPATH , '//*[@id="hotel-checkin-hp-hotel"]')
    Check_out = (By.XPATH, '//*[@id="hotel-checkout-hp-hotel"]')
    # ---------------------------------------------
    Rooms = (By.XPATH, '//*[@id="hotel-rooms-hp-hotel"]')
    Adults = (By.XPATH, '//*[@id="hotel-rooms-hp-hotel"]')
    Children = (By.XPATH, '//*[@id="hotel-1-children-hp-hotel"]')
    Search = (By.XPATH, '//div[8]/label/button')
    # -----------------------
    Hotels = (By.CSS_SELECTOR, 'a.flex-link')
    Reserve = (By.ID, 'mock-book-button')
    Reserve_recom = (By.XPATH, '//*[@id="rooms-and-rates"]/div/article/table/tbody[1]/tr/td[3]/div/form/div[1]/button')
    # -----------------------
class Check:
    Hotel = (By.CLASS_NAME, "section-header-main")
    Finish = (By.ID, "secondary-content")