#  -*- coding: utf-8-*-                                                                                             #
# Python 3.x.x
#----------------------------------------------
# The script demonstrates the recording of traffic for firefox
#   and chrome through browsermobproxy
# Src: https://automated-testing.info/t/chto-takoe-browsermob-proxy-i-kak-zastavit-ego-rabotat-tutorial-dlya-nachinayushhih-primer-ispolzovaniya-na-python/3510
#----------------------------------------------
PATH_SERVER = r"c:\Program Files (x86)\browsermob-proxy\bin\browsermob-proxy"
PATH_DRIVER_FIREFOX = r'd:\WORK_MC_21\Tester\Auto_Tester\Drivers\geckodriver.exe'
PATH_DRIVER_CHROME = r'd:\WORK_MC_21\Tester\Auto_Tester\Drivers\chromedriver.exe'
PATH_SITE = r'https://yandex.ru'

from browsermobproxy import Server, Client
from selenium import webdriver
import time, json, pprint, sys
#----------------------------------------------

def example_1():
    """Recording traffic in json for firefox"""

    # run server
    server = Server(PATH_SERVER)
    server.start()

    # run proxy and webdriver
    proxy = server.create_proxy()
    profile = webdriver.FirefoxProfile()
    profile.set_proxy(proxy.selenium_proxy())
    driver  = webdriver.Firefox(firefox_profile=profile,\
                                executable_path=PATH_DRIVER_FIREFOX)

    proxy.new_har(PATH_SITE, options={'captureHeaders': True})
    driver.get(PATH_SITE)
    driver.find_element_by_xpath('//*[@id="text"]').send_keys('Weather Taganrog')
    driver.find_element_by_xpath('//div[@class="search2__button"]/*').click()
    #------------------------------------------------------------
    # get object proxy.har and recording
    result = json.dumps(proxy.har, ensure_ascii=False)

    # can out in *.json object
    # sys.stdout = open('browsermobproxy_firefox.json', 'w')
    # pprint.pprint(result) # pprint - smart line-wrap output

    sys.stdout = open('browsermobproxy_firefox.har', 'w') # redirecting the stream
    pprint.pprint(proxy.har)
    sys.stdout = sys.__stdout__ # returns the standarts stream
    # ------------------------------------------------------------

    # close and exit
    proxy.close()
    server.stop()
    time.sleep(2)
    driver.quit()
#-----------------------------------------------------
def example_2():
    """Recording traffic in json for chrome"""

    # run server
    server = Server(PATH_SERVER)
    server.start()
    proxy = server.create_proxy()

    # run proxy and webdriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
    driver = webdriver.Chrome(chrome_options=chrome_options, \
                              executable_path=PATH_DRIVER_CHROME)
    proxy.new_har("google")


    driver.get("https://www.google.ru")
    driver.find_element_by_id('lst-ib').send_keys('Weather Taganrog')
    driver.find_element_by_id('lst-ib').send_keys(u'\ue007')

    # get har object proxy.har and recording
    sys.stdout = open('browsermobproxy_chrome.har', 'w') # redirecting the stream
    pprint.pprint(proxy.har) # pprint - smart line-wrap output
    sys.stdout = sys.__stdout__ # returns the standarts stream

    # close and exit
    server.stop()
    time.sleep(2)
    driver.quit()

#-----------------------------------------------------
if '__main__' == __name__:
    example_1()
    example_2()

    pass