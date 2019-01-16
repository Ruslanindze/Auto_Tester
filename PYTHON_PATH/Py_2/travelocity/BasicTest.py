#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Скрипт с базовым классом, наследуясь от которого можно писать сразу тесты
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
    # ---------------------------
    @classmethod
    def setUpClass(cls):
        cls.Driver = DM.Driver_Manager(cls.Browser).driver
        cls.Driver = Log.LogListener.get_ef_driver(cls.Driver)
    # # ---------------------------
    # def setUp(self):
    #     self.Driver._listener.get_method_name(self.id())
    # # ---------------------------
    # def run(self, result=None):
    #     self.currentResult = result  # remember result for use in tearDown
    #     unittest.TestCase.run(self, result)  # call superclass run method
    # # ---------------------------
    # def tearDown(self):
    #     # -------------- для логирования упавших тестов
    #     time.sleep(2)
    #     self.find_err = False
    #     for method, error in self._outcome.errors:
    #         if error:
    #             self.find_err = True
    #             self.Driver._listener.on_exception(error, self.Driver)
    #
    #     time.sleep(1)
    #     if self.find_err:
    #         allure.attach('screenshot', \
    #                       self.Driver.get_screenshot_as_png(),
    #                       type=AttachmentType.PNG)
    #     # -------------- для логирования упавших тестов
    # # ---------------------------
    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.Driver.quit()
#--------------------------------