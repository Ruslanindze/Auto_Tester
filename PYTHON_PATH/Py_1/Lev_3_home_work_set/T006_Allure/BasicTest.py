#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import time, os, unittest, allure
from allure.constants import AttachmentType

import T006_Allure.DriverManager as DM
import T006_Allure.PageObjC as Obj
import T006_Allure.LoggerC as Log
import T006_Allure.Str_Const as SC
#---------------------------------
class BasicTest(unittest.TestCase):
    Browser = None
    Driver = None
    Path_Video = None
    # ------------------------------
    @classmethod
    def setUpClass(cls):
        cls.driver = Log.LogListener.get_ef_driver(\
            DM.Driver_Manager(cls.Browser).driver)
        cls.HomeP = Obj.Home(cls.driver)
    # ------------------------------
    def setUp(self):
        self.driver._listener.get_method_name(self.id())

        self.Path_Video = os.path.join(SC.PATH_VIDEO, \
                                       '{}.flv'.format(self.id()))
        self.VideoRec = Log.VideoRecorder(SC.PATH_FFMPEG, self.Path_Video)
        self.VideoRec.start()
    # ------------------------------
    def run(self, result=None):
        self.currentResult = result  # remember result for use in tearDown
        unittest.TestCase.run(self, result)  # call superclass run method
    # -----------------------------------
    def tearDown(self):
        # -------------- для логирования упавших тестов
        time.sleep(2)
        self.find_err = False
        for method, error in self._outcome.errors:
            if error:
                self.find_err = True
                self.driver._listener.on_exception(error, self.driver)

        self.VideoRec.stop()

        time.sleep(1)
        if not self.find_err:
            if os.path.exists(self.Path_Video):
                os.remove(self.Path_Video)
        else:
            allure.attach('screenshot', \
                          self.driver.get_screenshot_as_png(),
                          type=AttachmentType.PNG)
            # allure.attach('video', \
            #               type)
        # -------------- для логирования упавших тестов
    # -----------------------------------
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
    # ------------------------------------------------