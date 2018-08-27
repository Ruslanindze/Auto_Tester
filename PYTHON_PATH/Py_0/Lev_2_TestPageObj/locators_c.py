#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
from selenium.webdriver.common.by import By
#--------------------------------
class Common:
    """Здесь описаны общие локаторы"""
    BlueButton = (By.XPATH, '//*[@class = "btn btn-primary"]')
    TravelTheWorld = (By.XPATH, '//a[text()="Travel The World"]')
    BlazeDemo = By.CLASS_NAME, "navbar-brand"
    home = (By.XPATH, '//a[text()="home"]')
    #--------------------------------------
    LoginUp = By.XPATH, '//a[text()="Login"]'
    RegisterUp = By.XPATH, '//a[text()="Register"]'
    # --------------------------------------
    Email = By.ID, "email"
    Password = By.ID, "password"
    RememberMe = By.NAME, "remember"
    # --------------------------------------
    Dropdown_List = By.TAG_NAME, 'option'
#--------------------------------
class Home:
    """Здесь описаны локаторы для домащней страницы"""
    TravelTheWorld = Common.TravelTheWorld
    home = Common.home
    link_picture = By.XPATH, '//a[text()="destination of the week! The Beach!"]'
    departure_city = By.NAME, 'fromPort'
    destination_city = By.NAME, 'toPort'
    BlueButton = Common.BlueButton
    Dropdown_List = Common.Dropdown_List
#------------------------------------
class Login:
    BlazeDemo = Common.BlazeDemo
    LoginUp = Common.LoginUp
    RegisterUp = Common.RegisterUp
    # ------------------
    Email = Common.Email
    Password = Common.Password
    RememberMe = By.NAME, "remember"
    BlueButton = Common.BlueButton
    ForgotPassword = By.PARTIAL_LINK_TEXT, "Forgot Your Password?"
#------------------------------------
class Register:
    BlazeDemo = Common.BlazeDemo
    LoginUp = Common.LoginUp
    RegisterUp = Common.RegisterUp
    # ------------------
    Name = By.ID, "name"
    Company = By.ID, "company"
    Email = Common.Email
    Password = Common.Password
    Confirm_Password = By.ID, "password-confirm"
    BlueButton = Common.BlueButton
#------------------------------------
class Reset:
    BlazeDemo = Common.BlazeDemo
    LoginUp = Common.LoginUp
    RegisterUp = Common.RegisterUp
    Email = Common.Email
    BlueButton = Common.BlueButton
# ------------------------------------
class Find_Flights:
    TravelTheWorld = Common.TravelTheWorld
    home = Common.home
    Choose_Several = By.CLASS_NAME, 'btn btn-small'
# ------------------------------------
class Purchase:
    TravelTheWorld = Common.TravelTheWorld
    home = Common.home
    Name = By.ID, "inputName"
    Address = By.ID, "address"
    City = By.ID, "city"
    State = By.ID, "state"
    ZipCode = By.ID, "zipCode"
    CardType = By.ID ,"cardType"
    CreditCardNumber = By.ID, "creditCardNumber"
    Month = By.ID, "creditCardMonth"
    Year = By.ID, "creditCardYear"
    NameonCard = By.ID, "nameOnCard"
    RememberMe = Common.RememberMe
    BlueButton = Common.BlueButton
#------------------------