#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#------------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#------------------------------------
import unittest, os, sys
from T001_WinFrame.BasicTest import Basic_UniT as BT
#------------------------------------
DIR_RUN = os.getcwd()
AU3_PATH = os.path.join(DIR_RUN, 'au3\choose_pict.exe')
PICT_PATH = os.path.join(DIR_RUN, 'au3\pict.jpg')
#------------------------------------
def open_pict(path_pict):
    try:
        os.system('{} {}'.format(AU3_PATH, path_pict))
    except Exception as e:
        print(e)
        os._exit()
#------------------------------------
class Test_TransP(BT):
    Path_Pict = PICT_PATH
    asser_text = """Приветствовать
Рад, что вы приехали!"""
    def test_A(self):
        """Проверка перевода слов с картинки"""
        # Вызываем окно для выбора картинки со словами для перевода (En -> Ru)
        self.choose_file = self.TranslateP.choose_file
        self.choose_file.click()

        # В диалоговом окне выбираем картинку и загружаем её
        open_pict(self.Path_Pict)

        # Жмакаем "Открыть в переводчик"
        self.open_translate = self.TranslateP.open_translateT
        self.open_translate.click()

        # Считываем текст перевода в новой вкладке
        tab = self.driver.window_handles[1] # нужная нам вкладка
        self.driver.close() # закрываем 1-ю вкладку
        self.driver.switch_to.window(tab) # переключаем драйвер на др. вкладку
        self.language = self.TranslateP.get_lang_translate(self.driver)
        self.translate = self.TranslateP.get_translate(self.driver) # получаем перевод

        # print("\n{}\n{}\n{}\n".format('*' * 50, self.translate, '*' * 50))

        # зона проверок языка и текста перевода
        self.assertEqual("русский", self.language.lower())
        self.assertEqual(self.asser_text, self.translate)
#------------------------------------

if '__main__' == __name__:    unittest.main()