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
    def on_exception(self, exception, driver):
        logging.error('#ERROR: {}'.format(exception))
        driver.get_screenshot_as_file('{}.png'.format(__file__[:-3]))

#------------------------------------------
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # creating  web driver with _listener for log tests
        driver = webdriver.Chrome(PATH_DRIVER_CHROME) # creating ussually driver
        cls.driver = EventFiringWebDriver(driver, LogListener()) # creating driver with _listener

        # setting logging
        logging.basicConfig(format='%(asctime)s %(message)s', \
                            datefmt='%m/%d/%Y %I:%M:%S %p',\
                            filename= '{}.log'.format(__file__[:-3])) # __file__ - имя скрипта

    def test_A(self):
        """Testing Google title in driver"""

        # The test will be OK
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def test_B(self):
        """Testing Yandex title in driver but with bad parameter"""

        # The test will be KO for check functions logger
        self.driver.get("http://www.yandex.ru")
        self.assertEqual(self.driver.title, "Yandex")

    def tearDown(self):
        # if error, then call _listener
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