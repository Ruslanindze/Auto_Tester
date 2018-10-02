#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
from selenium.webdriver.common.by import By
#--------------------------------
class Text:
    """Здесь описаны локаторы для переводчика яндекс в разделе ТЕКСТ"""
    left_pane_tr    = By.ID, 'fakeArea'
    left_pane_lang  = By.ID, 'srcLangButton'
    right_pane_tr   = By.XPATH, '//*[@id="textbox2"]/div'
    right_pane_lang = By.ID, 'dstLangButton'
    switch_dir      = By.XPATH, '//div[@role="button" and contains(@class, "button")]'
# --------------------------------
class Site:
    """Здесь описаны локаторы для переводчика яндекс в разделе САЙТ"""
    original    = By.ID, 'srcLangButton'
    translation = By.ID, 'dstLangButton'
    input_site  = By.ID, 'urlInput'
    translate   = By.XPATH, '//*[@id="url"]/span[2]'
# --------------------------------
class Picture:
    """Здесь описаны локаторы для переводчика яндекс в разделе КАРТИНКА"""
    choose_file = By.XPATH, '//span[@class="link"]'
    from_lang   = By.ID, 'sourceLangButton'
    to_lang     = By.ID, 'targetLangButton'
    switch_dir  = By.XPATH, '//span[contains(@class, "button_icon_swap")]'
    open_in_tr  = By.XPATH, '//div[contains(@class, "toolbar-group")][4]'
# --------------------------------
class Comm:
    """ЗДесь описывабтся локаторы общих элементов"""
    logo = By.ID, 'logo'
    text = By.XPATH, '//div/*[text()="Текст"]'
    site = By.XPATH, '//div/*[text()="Сайт"]'
    pict = By.XPATH, '//div/*[text()="Картинка"]'

