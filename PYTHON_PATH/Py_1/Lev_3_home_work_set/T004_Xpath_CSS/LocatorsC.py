#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
from selenium.webdriver.common.by import By
#--------------------------------
class Xpath_Header():
    """Здесь описаны локаторы для домащней страницы элементов NAV-BAR"""
    Mail_Btn = (By.XPATH, '//div[@id="app"]//div[@class="rui-Topline-menu"]/a[1]')
    News_Btn = (By.XPATH, '//div[@class="rui-Topline-menu"]/a[position()=2]')
    Film_Btn = (By.XPATH, '//a[@class="rui-Topline-link rui-Topline-menuItem"][3]')
    Sport_Btn = (By.XPATH, '//a[@data-cerber-topline][4]')
    Car_Btn = (By.XPATH, '//a[contains(@data-cerber-topline, "auto_media")]')
    ShowB_Btn = (By.XPATH, '//ancestor::a[starts-with(@data-cerber-topline, "projects::st")][parent::div[@class="rui-Topline-menu"]]')
    Games_Btn = (By.XPATH, '//div[@class = "rui-Topline-toplineContainer"]/*/a[last()]')
    Yet_Btn = (By.XPATH, '(//a/following-sibling::button)[1]')
    Yet_Ya = (By.XPATH, '//ancestor::div[@class="promo__text"]/parent::a')
    Src_Btn = (By.XPATH, '//div[contains(@data-cerber-topline, "search::open")]')
    Int_Btn = (By.XPATH, '//div[parent::div[contains(@class, "rui-ToplineUser-root rui")]]')
    Src_String = (By.xpath, '(//input[@type="text"])[2]')
    Example = (By.XPATH, '//div[@class="_2ncf"]')
#------------------------------------
class CSS_Header():
    Mail_Btn = By.CSS_SELECTOR, 'div.rui-Topline-menu > a:nth-child(1)'
    News_Btn = By.CSS_SELECTOR, 'div.rui-Topline-menu > a:nth-child(1)+a'
    Film_Btn = By.CSS_SELECTOR, 'div.rui-Topline-menu > a:nth-of-type(3)'
    Sport_Btn = By.CSS_SELECTOR, 'div#app a[data-cerber-topline$="kino"]'
    Car_Btn = By.CSS_SELECTOR, 'a[class="rui-Topline-link rui-Topline-menuItem"][data-cerber-topline="projects::auto_media"]'
    ShowB_Btn = By.CSS_SELECTOR, 'a[data-cerber-topline*="::star"]'
    Games_Btn = By.CSS_SELECTOR, 'div.rui-Topline-toplineContainer > * >a:nth-child(7)'
    Yet_Btn = By.CSS_SELECTOR, 'div > button.rui-Topline-moreButton'
    Yet_Ya = By.CSS_SELECTOR, 'div.promo__text'
    Src_Btn = By.CSS_SELECTOR, 'svg.rui-ToplineSearch-inlineSearchIcon'
    Int_Btn = By.CSS_SELECTOR, 'div[data-cerber-topline^="user"] > *'
    Src_String = By.CSS_SELECTOR, 'div > input[type="text"][class="rui-ComplexSearch-input"]'
    Example = By.CSS_SELECTOR, 'div._2ncf > a'
#------------------------------------