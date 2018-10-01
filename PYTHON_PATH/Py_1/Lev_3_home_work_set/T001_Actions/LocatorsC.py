#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Скрипт с локаторами без логики
#--------------------------------
from selenium.webdriver.common.by import By
#--------------------------------
class Home:
    ContactUs = (By.XPATH, '//*[@id="contact-link"]/a')
    SignIn    = (By.CSS_SELECTOR, 'nav > div.header_user_info > a')
    GetSav    = (By.CSS_SELECTOR, 'div.banner > div > div > a > img')
    YourLogo  = (By.XPATH, '//*[@id="header_logo"]/a/img')
    Search    = (By.ID, 'search_query_top')
    Cart      = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a')
    Women     = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
    Dresses   = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
    T_shirts  = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
    #--------------------------------------------
    Shop_Now  = (By.XPATH, '//*[@id="homeslider"]/li[4]/div/p[2]/button')
    Shop_Prev = (By.XPATH, '//*[@id="homepage-slider"]/div/div[2]/div/a[1]')
    Shop_Next = (By.XPATH, '//*[@id="homepage-slider"]/div/div[2]/div/a[2]')
    Off_25    = (By.XPATH, '//*[@id="htmlcontent_top"]/ul/li[1]/a/img')
    Off_45    = (By.XPATH, '//*[@id="htmlcontent_top"]/ul/li[2]/a/img')
    Popular   = (By.XPATH, '//*[@id="home-page-tabs"]/li[1]/a')
    Best_sell = (By.XPATH, '//*[@id="home-page-tabs"]/li[2]/a')
    Price_pic = (By.XPATH, '//*[@id="homefeatured"]//li/div')
    Pict_down = (By.XPATH, '//*[@id="htmlcontent_home"]/ul/li[1]/a/img')
    #--------------------------------------------
    Face_Pres = (By.CSS_SELECTOR, 'div._1dro._2ph-.clearfix > a > img')
    Face_Like = (By.XPATH, '//*[@id="u_0_2"]/a[1]')
    Face_Shar = (By.XPATH, '//*[@id="u_0_3"]/button')
    Face_Sel  = (By.XPATH, '//*[@id="cmsinfo_block"]/div[1]/ul/li[2]/div/p/a')
    Inp_email = (By.CSS_SELECTOR, '#newsletter-input')
    Email_next= (By.CSS_SELECTOR, '#newsletter_block_left > div > form > div > button')
    Follow_Us = (By.XPATH, '//*[@id="social_block"]/ul/li')
    #---------------------------------------------
    CategorS  = (By.XPATH, '//*[@id="footer"]/div/section[2]/div')
    InfoS     = (By.XPATH, '//*[@id="footer"]/div/section[3]/ul/li')
    MyAccS    = (By.XPATH, '//*[@id="footer"]/div/section[5]/div/ul/li')
    Sup_email = (By.CSS_SELECTOR, 'li:nth-child(3) > span > a')
    DownLink  = (By.XPATH, '//*[@id="footer"]/div/section[4]/div/a')
#------------------------------------