#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Тестируем API запросы
#--------------------------------
import sys, os
PATH_IMPORT = os.getcwd()[:os.getcwd().rfind('\\')]
if PATH_IMPORT not in sys.path:
    sys.path.append(PATH_IMPORT)
#--------------------------------
import unittest
import pprint
import requests
from YaTranslate_API.BasicTest import Basic_UniT as BT
import YaTranslate_API.Str_Const as SC
#--------------------------------
DICT_A = {"key":SC.YA_API_KEY, "ui":None}
DICT_B = {"key":SC.YA_API_KEY, "lang":None, "text":None}
STATUS_OK = 200
#--------------------------------
def setUpModule():
    print("Implementation of the setUpModule()")

def tearDownModule():
    print("Implementation of the tearDownModule()")
# -------------------------------
class Test_Api(BT):
    """Check of the languages support"""
    def test_A(self):
        print("Implementation of the case {}".format(self.id()))

        for id, name in SC.DICT_LANG.items():

            with self.subTest(lang_name = name):
                DICT_A['ui'] = id
                req = requests.get(SC.YA_API_URL, DICT_A)

                self.assertEqual(req.status_code, STATUS_OK, 'Bad request status for language "{}" ...'.format(name))

                self.assertEqual(len(req.json()['langs']), len(SC.DICT_LANG), 'List of supported languages \
                    is not complete for "{}"'.format(name))
    # -------------------------------
    def test_B(self):
        """Check of translation"""
        print("Implementation of the case {}".format(self.id()))

        for i, obj in enumerate(SC.LIST_TRANSLATE):

            with self.subTest(lang_name = '{}, {}'.format(obj[0], obj[1])):
                DICT_B['lang'] = obj[0]
                DICT_B['text'] = obj[1]
                req = requests.get(SC.YA_API_URL_TR, DICT_B)

                self.assertEqual(req.status_code, STATUS_OK, \
                            'Bad status translate for lang ={}, text = {}'\
                             .format(obj[0], obj[1]))

                self.assertEqual(req.json()['text'][0], SC.LIST_EXPECTED[i])
# ----------------------------------------------


#-----------------------------------------------
if '__main__' == __name__:
    unittest.main(verbosity=2)
    # python Test_API_YaTr.py -v
