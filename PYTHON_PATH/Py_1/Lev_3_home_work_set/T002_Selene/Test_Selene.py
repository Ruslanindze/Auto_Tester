#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
from selene.api import *
from T002_Selene.PageObj import *
from T002_Selene.Str_Const import *
import T002_Selene.DriverManager as DM
import time
#--------------------
def test_A(new_driver):
    """Структурное использования Selene"""
    browser.set_driver(new_driver)

    Obj_Test = Page_Objects()
    Obj_Test.open()
    browser.should(have.url(HOME_PAGE))

    Obj_Test.inventory.click()
    browser.should(have.url(INVEN_PAGE))

    Obj_Test.matrix_ideas.click()
    browser.should(have.url_containing(MATR_PAGE))

    Obj_Test.input_idea.set(IDEA).should(have.value(IDEA))
    Obj_Test.butt_get_idea.click()

    time.sleep(3)
    browser.quit()
#--------------------
def test_B(new_driver):
    """Испозьзования цепочки в тестах с Selene"""
    browser.set_driver(new_driver)

    (Page_Objects()
     .open()
     .go_inventory()
     .go_matrix_ideas()
     .input_ideas(IDEA)
     .should(have.value(IDEA))
    )

    time.sleep(5)
    browser.quit()
#--------------------

#--------------------
if '__main__' == __name__:
    list_browsers = ['chrome']
    for name_browser in list_browsers:
        # test_A(DM.Driver_Manager(name_browser).driver)
        test_B(DM.Driver_Manager(name_browser).driver)