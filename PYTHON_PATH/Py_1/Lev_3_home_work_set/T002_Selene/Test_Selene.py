#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
from selene.api import *
from T002_Selene.PageObj import *
from T002_Selene.Str_Const import *
import T002_Selene.DriverManager as DM
import time
#--------------------
def test_A(new_driver):
    """Структурный вид проверки Матрицы идей с помощью Selene"""
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
    """Попытка реализации теста в виде цепочки с помощью Selene"""
    browser.set_driver(new_driver)

    (Page_Objects()
     .open() # открыли домашнюю страницу
     .go_inventory() # перешли в пункт Ивентарь
     .go_matrix_ideas() # выбрали раздел Матрица Идей
     .input_ideas(IDEA) # ввели идею
     .should(have.value(IDEA)) # проверяем, что проверяемый элемент имеет нужное знач.
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