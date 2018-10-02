#  -*- coding: cp1251 -*-                                                                                             #
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
    Reserve = (By.XPATH, '//*[@id="mock-book-button"]')
    Reserve_recom = (By.XPATH, '(//div[@class="book-button-wrapper "]/button)[1]')