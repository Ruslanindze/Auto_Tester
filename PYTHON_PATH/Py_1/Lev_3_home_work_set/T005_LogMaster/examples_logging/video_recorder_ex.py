#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
#--------------------------------

PATH_DRIVER_CHROME = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"
PATH_VIDEO = r'd:\WORK_MC_21\Tester\Auto_Tester\PYTHON_PATH\Py_1\Lev_3_home_work_set\T005_LogMaster\examples_logging\video.mp4'

import unittest, time, datetime, logging
from selenium import webdriver
from test_recorder.video_recorder import VideoRecorder
#------------------------------------------

#------------------------------------------
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # �������� ����������� � _listener ��� ����������� ������
        cls.driver = webdriver.Chrome(PATH_DRIVER_CHROME) # �������� �������� ��������
        cls.video_record = VideoRecorder()
        cls.video_record.start_recording()

    def test_A(self):
        """Testing Google title in driver"""

        # ���� ������ �� ��
        self.driver.get("http://www.google.com")
        self.driver.find_element_by_id('lst-ib').send_keys('������ ��������')
        self.driver.find_element_by_id('lst-ib').send_keys(u'\ue007')

    def test_B(self):
        """Testing Yandex title in driver but with bad parameter"""

        # ���� ���������� ��������� ��� ������������ ����������� ������� �����������
        self.driver.get("http://www.yandex.ru")
        self.assertEqual(self.driver.title, "�����")
        self.driver.find_element_by_xpath('//*[@id="text"]').send_keys('������ ��������')
        self.driver.find_element_by_xpath('//div[@class="search2__button"]/*').click()

    def tearDown(self):
        # ���� � ����� ����� self �� ������ ����� ���������� ����������, ��
        # ��������� ����� on_exception ������� ������ LogListener
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.video_record.stop_recording()
        cls.driver.quit()

#----------------------------------------
if '__main__' == __name__:
    unittest.main()