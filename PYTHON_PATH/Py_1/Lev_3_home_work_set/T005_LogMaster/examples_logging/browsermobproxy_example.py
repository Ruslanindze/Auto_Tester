#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#----------------------------------------------
# Src: https://automated-testing.info/t/chto-takoe-browsermob-proxy-i-kak-zastavit-ego-rabotat-tutorial-dlya-nachinayushhih-primer-ispolzovaniya-na-python/3510
#----------------------------------------------
PATH_SERVER = r'c:\Users\dudnikov\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\browsermobproxy'

from browsermobproxy import Server
server = Server(PATH_SERVER)
server.start()
