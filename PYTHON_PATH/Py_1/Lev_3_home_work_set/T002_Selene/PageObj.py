#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------
from selene.api import *
from T002_Selene.Str_Const import *
#--------------------
class Page_Objects(object):
    def __init__(self):
        self.inventory = s(by.xpath(Inventory_Xpath))
        self.matrix_ideas = s(Matrix_Selec)
        self.input_idea = s(by.xpath(Input_Idea_Xpath))
        self.butt_get_idea = s(by.xpath(Get_Idea_Xpath))
        self.see_ideas = ss(by.xpath(See_Ideas_Xpath))
    #--------------------------
    def open(self):
        browser.open_url(HOME_PAGE)
        return self
    def go_inventory(self):
        self.inventory.click()
        return self
    def go_matrix_ideas(self):
        self.matrix_ideas.click()
        return self
    def input_ideas(self, idea):
        self.input_idea.set(idea)
        self.butt_get_idea.click()
        return self.input_idea