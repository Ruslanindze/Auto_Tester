#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Реализован класс-родитель, для того, чтобы наследовать и писать тесты
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import time, unittest, allure
import travelocity.DriverManager as DM
import travelocity.Str_Const as SC
import travelocity.LoggerC as Log

from allure.constants import AttachmentType
#--------------------------------

#--------------------------------
class Basic_UniT(unittest.TestCase):
    Browser =  None
    Driver = None
    Driver_Ef = None
    # ---------------------------
    @classmethod
    def setUpClass(cls):
        # создание веб-драйвера
        cls.Driver = DM.Driver_Manager(cls.Browser).driver
        # создание драйвера с прослушкой событий (для их переопределений)
        cls.Driver_Ef = Log.LogListener.get_ef_driver(cls.Driver)
    # ---------------------------
    def setUp(self):
        self.Driver_Ef._listener.get_method_name(self.id())
    # ---------------------------
    def run(self, result=None):
        # Для мониторинга прогона (сколько ОК, КО и т.д)
        self.currentResult = result  # remember result for use in tearDown
        unittest.TestCase.run(self, result)  # call superclass run method
    # ---------------------------
    def tearDown(self):
        # -------------- зона ловли ошибок
        time.sleep(1)
        self.find_err = False
        for method, error in self._outcome.errors:
            if error:
                self.find_err = True
                self.Driver_Ef._listener.on_exception(error, self.Driver)

        time.sleep(1)
        if self.find_err:
            allure.attach('screenshot', \
                          self.Driver_Ef.get_screenshot_as_png(),
                          type=AttachmentType.PNG)
            # -------------- зона ловли ошибок
    # ---------------------------
    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.Driver.quit()
#--------------------------------