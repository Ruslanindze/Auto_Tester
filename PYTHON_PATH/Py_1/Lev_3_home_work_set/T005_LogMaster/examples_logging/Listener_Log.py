#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# This way of logging seemed to me the most appropriate.
# Demonstrated here screwing onto your webdriver _listener
#   through EventFiringWebDriver and inheriting from AbstractEventListener,
#   when brewing a test or other unexpected error
#   a screenshot is taken in the format .png and recorded in *.log library forces
#   logging.
# You can also override methods in the Log Listener(Abstract EventListener) class
#   and to specify the logging (n: before_click, after_change_value_of etc)
# This method was made under the style of java - >
#   class EventListener implements WebDriverEventListener...
#--------------------------------

PATH_DRIVER_CHROME = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"

import unittest, time, datetime, logging
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener

#------------------------------------------
class LogListener(AbstractEventListener):
    """This class is necessary for add to the web driver  method _listener"""
    count = 0
    method_name = None
    #---------------------------------------
    def __init__(self):
        log = open('{}.log'.format(__file__[:-3]), "w",\
                   encoding='utf-8')
        handler = logging.StreamHandler(log)
        formatter = logging.Formatter(\
            u'# %(levelname)-8s [%(asctime)s]#  %(funcName)-13s -> %(message)s')
        handler.setFormatter(formatter)
        self.logger = logging.getLogger()
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    #---------------------------------------
    def get_method_name(self, method_name):
        self.method_name = method_name

    def before_click(self, element, driver):
        self.logger.info('{}: {}'.format(self.method_name, element))

    def before_find(self, by, value, driver):
        self.logger.info('{}: {} {}'.format(self.method_name, by, value))

    def after_find(self, by, value, driver):
        self.logger.info('{}: {} {} '.format(self.method_name, by, value))

    def on_exception(self, exception, driver):
        self.logger.error('{}: {}'.format(self.method_name, exception))
        driver.get_screenshot_as_file('{}_{}.png'.format(__file__[:-3], \
                                                        self.count))
        self.count += 1
#------------------------------------------
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # creating  web driver with _listener for log tests
        driver = webdriver.Chrome(PATH_DRIVER_CHROME) # creating ussually driver
        cls.driver = EventFiringWebDriver(driver, LogListener()) # creating driver with _listener

    def setUp(self):
        self.driver._listener.get_method_name(self.id())

    def test_A(self):
        """Testing Google title in driver"""

        # The test will be OK
        self.driver.get("http://www.google.com")

        self.assertEqual(self.driver.title, "Google")

        elem = self.driver.find_element_by_xpath('//input[@name="btnI"]')
        elem.click()

    def test_B(self):
        """Testing Yandex title in driver but with bad parameter"""

        # The test will be KO for check functions logger
        self.driver.get("http://www.yandex.ru")

        elem = self.driver.find_element_by_xpath('//*[@data-id="video"]')
        elem.click()

        self.assertEqual(self.driver.title, "Яндекс")

    def tearDown(self):
        time.sleep(2)

        for method, error in self._outcome.errors:
            if error:
                self.driver._listener.on_exception(error, self.driver)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

#----------------------------------------
if '__main__' == __name__:
    unittest.main()