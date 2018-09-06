#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#----------------------------------------------
# Скрипт демонстрирует запись трафика для firefox
#   и chrome через browsermobproxy
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
    """Пишет из json в файл для firefox"""

    # запускаем сервер
    server = Server(PATH_SERVER)
    server.start()

    # запускаем proxy и вебдрайвер
    proxy = server.create_proxy()
    profile = webdriver.FirefoxProfile()
    profile.set_proxy(proxy.selenium_proxy())
    driver  = webdriver.Firefox(firefox_profile=profile,\
                                executable_path=PATH_DRIVER_FIREFOX)
    proxy.new_har(PATH_SITE, options={'captureHeaders': True})
    driver.get(PATH_SITE)
    driver.find_element_by_xpath('//*[@id="text"]').send_keys('Погода Таганрог')
    driver.find_element_by_xpath('//div[@class="search2__button"]/*').click()
    #------------------------------------------------------------
    # получаем json объект proxy.har и записываем 3-мя способами
    result = json.dumps(proxy.har, ensure_ascii=False)
    # with open('browsermobproxy_json.har', 'w') as file:
    #     json.dump(result, file)
    #
    # myfile = open('browsermobproxy_str.har', 'w')
    # myfile.write(str(proxy.har))
    # myfile.close()

    sys.stdout = open('browsermobproxy_firefox.json', 'w') #  перенаправляем поток
    pprint.pprint(result) # pprint - умный вывод, сам переносит строки
    sys.stdout = sys.__stdout__ # возращаем стандартный поток
    # ------------------------------------------------------------

    # выход
    proxy.close()
    server.stop()
    time.sleep(2)
    driver.quit()
#-----------------------------------------------------
def example_2():
    """Пишет из json в файл для chrome"""
    server = Server(PATH_SERVER)
    server.start()
    proxy = server.create_proxy()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
    driver = webdriver.Chrome(chrome_options=chrome_options, \
                              executable_path=PATH_DRIVER_CHROME)

    proxy.new_har("google")
    driver.get("https://www.google.ru")
    driver.find_element_by_id('lst-ib').send_keys('Погода Таганрог')
    driver.find_element_by_id('lst-ib').send_keys(u'\ue007')

    result = json.dumps(proxy.har)
    sys.stdout = open('browsermobproxy_chrome.json', 'w') #  перенаправляем поток
    pprint.pprint(result) # pprint - умный вывод, сам переносит строки
    sys.stdout = sys.__stdout__ # возращаем стандартный поток

    server.stop()
    time.sleep(2)
    driver.quit()

#-----------------------------------------------------
if '__main__' == __name__:
    example_1()
    example_2()

    pass