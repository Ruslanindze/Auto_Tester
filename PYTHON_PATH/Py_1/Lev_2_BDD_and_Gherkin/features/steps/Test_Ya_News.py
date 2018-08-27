#----------------------
import sys
sys.path.append(r'd:\WORK_MC_21\Tester\Auto_Tester\PYTHON_PATH\Py_1\Lev_2_BDD_and_Gherkin')
#----------------------
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, unittest
import BasicTest as BT

class Test_Ya_News(BT.Basic_UniT):

    @given('website "{url}"')
    def step_given(context, url):
        # context.browser = BT.Basic_UniT.Driver
        context.browser.maximize_window()
        context.browser.get(url)

    @when('user push button with text "{butt_text}"')
    def step_when(context, butt_text):
        context.butt_news = WebDriverWait(context.browser, 3).until(
            EC.element_to_be_clickable((By.LINK_TEXT, butt_text)))
        context.butt_news.click()

    @then('the current url "{url}"')
    def step_then(context, url):
        assert url == context.browser.current_url