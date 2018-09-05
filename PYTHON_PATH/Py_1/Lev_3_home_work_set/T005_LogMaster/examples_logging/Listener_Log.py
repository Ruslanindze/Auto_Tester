#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Этот способ логирования показался мне наиболее подходящим.
# Здесь продемонстрировано прикручивания к webdriver своего _listener
#   через EventFiringWebDriver и наследования от AbstractEventListener,
#   при заваливании теста или другой, непредвиденной, ошибки
#   делается скриншот в формате .png и записывается в *.log силами библиотеки
#   logging.
# Также в классе LogListener(AbstractEventListener) можно переопределять методы
#   и самому детализировать логгирование (н.: before_click, after_change_value_of и т.д)
# Данный способ был сделан под стиль java ->
#   class EventListener implements WebDriverEventListener...
#--------------------------------

PATH_DRIVER_CHROME = r"d:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe"

import unittest, time, datetime, logging
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener
#------------------------------------------

class LogListener(AbstractEventListener):
    """Данные класс необходим для прикручивания к webdriver своего _listener"""
    def on_exception(self, exception, driver):
        logging.error('#ERROR: {}'.format(exception))
        driver.get_screenshot_as_file('{}.png'.format(__file__[:-3]))

#------------------------------------------
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # создание вебдрайвера с _listener для логирования тестов
        driver = webdriver.Chrome(PATH_DRIVER_CHROME) # создание обычного драйвера
        cls.driver = EventFiringWebDriver(driver, LogListener()) # расширенный драйвер

        # настройка logging, необходим, чтобы тупо заменить обычный print
        logging.basicConfig(format='%(asctime)s %(message)s', \
                            datefmt='%m/%d/%Y %I:%M:%S %p',\
                            filename= '{}.log'.format(__file__[:-3])) # __file__ - имя скрипта

    def test_A(self):
        """Testing Google title in driver"""

        # Тест пройдёт на ОК
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def test_B(self):
        """Testing Yandex title in driver but with bad parameter"""

        # Тест специально завалится для демонстрации настроенной системы логирования
        self.driver.get("http://www.yandex.ru")
        self.assertEqual(self.driver.title, "Яндек")

    def tearDown(self):
        # если в самом тесте self на выходе будут обнаружены исключения, то
        # вызовется метод on_exception объекта класса LogListener
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