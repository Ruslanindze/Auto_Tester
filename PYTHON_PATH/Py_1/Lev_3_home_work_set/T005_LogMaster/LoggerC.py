#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Тут реализовано 3 класса-логгера, которые умеют:
# 1) LogListener - записывать события и exception в файл *.log;
# 2) записывать траффик в формат через pprint (*.har);
# 3) записывать видео в формате *.flv (иди др. формат)
#--------------------------------
import logging, sys, pprint, subprocess as subp

from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener

from browsermobproxy import Server, Client
from selenium import webdriver
#--------------------------------- zone LogListener
class LogListener(AbstractEventListener):
    """Класс отслеживает события и выводит в *.log, события переопределяются"""
    #---------------------------------------
    method_name = 'Unknown_name'
    cnt_t = 0
    cnt_f = 0
    cnt_p = 0
    # ---------------------------------------
    def __init__(self):
        """Инициализируется логгер с нужной кодировкой"""
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
    @staticmethod
    def get_ef_driver(driver):
        return  EventFiringWebDriver(driver, LogListener())  # creating driver with _listener
    # ---------------------------------------
    def get_method_name(self, method_name):
        """Логеру необходимо имя метода _listener.get_method_name()"""
        self.method_name = method_name

    def get_statis_tests(self, cnt_t, cnt_f ,cnt_p):
        self.cnt_t = cnt_t
        self.cnt_f = cnt_f
        self.cnt_p = cnt_p
    #---------------------------------------
    def before_find(self, by, value, driver):
        self.logger.info('{}: {} {}'.format(self.method_name, by, value))
    #---------------------------------------
    def before_click(self, element, driver):
        self.logger.info('{}: {}'.format(self.method_name, element))
    #---------------------------------------
    def before_change_value_of(self, element, driver):
        self.logger.info('{}: {}'.format(self.method_name,element))
    # ---------------------------------------
    def on_exception(self, exception, driver):
        self.logger.error('{}: {}'.format(self.method_name, exception))
        driver.get_screenshot_as_file('{}_{}.png'.format\
            (self.method_name[self.method_name.find('.')+1:], \
             self.on_exception.__name__))
    # ---------------------------------------
    def after_close(self, driver):
        logging.info(\
            'Statistique: TOTAL == {} , OK == {}, KO == {}'.\
            format(self.cnt_t, self.cnt_p, self.cnt_f))
    # ---------------------------------------
#--------------------------------- zone LogListener


#--------------------------------- zone LogMobProxy
class LogMobProxy():
    """Класс выводит траффик теста selenium"""
    def __init__(self, driver, path_server, browser='chrome'):
        self.server = Server(path_server)
        self.server.start()

        self.browser = browser
        self.create_proxy()

        self.driver = driver
        self.create_options() # create ChromeOptions or profile for Firefox
    #------------------------------------
    def create_proxy(self):
        self.proxy = self.server.create_proxy()

    def create_options(self):
        if 'chrome' == self.browser.lower():
            self.options = webdriver.FirefoxProfile()
            self.options.set_proxy(self.proxy.selenium_proxy())
        elif 'firefox' == self.browser.lower():
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--proxy-server={0}".\
                        format(self.proxy.proxy))

    def rec_traffic(self, file):
        sys.stdout = open(file, 'w')  # redirecting the stream
        pprint.pprint(self.proxy.har)
        sys.stdout = sys.__stdout__  # returns the standarts stream

    def stop_MobProxy(self):
        self.proxy.close()
        self.server.stop()
    # ------------------------------------
#--------------------------------- zone LogMobProxy


#--------------------------------- zone VideoRecorder
class VideoRecorder():
    """Необходим установленный ffmpeg в консоле"""
    #------------------------------------
    def __init__(self, path_ffmpeg_bin, path_video):
        command = [
            path_ffmpeg_bin,
            '-y',  # overwrite output files
            '-loglevel', 'error',
            '-f', 'gdigrab',
            # '-framerate', '12',   # default 30
            '-i', 'desktop',
            # '-t', '10',           # record or transcode "duration" seconds of audio/video
            '-s', '3000x1000',
            '-pix_fmt', 'yuv420p',
            '-c:v', 'libx264',
            '-profile:v', 'main',
            '-fs', '0.7M',  # set the limit file size in bytes
            path_video
        ]
    #------------------------------------
    def start(self):
        self.ffmpeg = subp.Popen(self.command, stdin=subp.PIPE, \
                        stdout=subp.PIPE, stderr=subp.PIPE)
    #------------------------------------
    def stop(self):
        self.ffmpeg.stdin.write("q".encode('utf-8'))
        self.ffmpeg.stdin.close()
#--------------------------------- zone VideoRecorder