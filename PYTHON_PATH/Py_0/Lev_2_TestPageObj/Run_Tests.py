#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
import unittest
import Py_0.Lev_2_TestPageObj.Home_Page_Test
import Py_0.Lev_2_TestPageObj.Login_Page_Test
#--------------------------------
def run_all():
    loader = unittest.TestLoader()
    loader.loadTestsFromTestCase()
    suite = loader.discover(start_dir='.', pattern='*Page_Test.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
#--------------------------------
def run_part_test():
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromNames(['Home_Page_Test',\
            'Login_Page_Test.Login_Page_Test.test_RegUp', \
            'Login_Page_Test.Login_Page_Test.test_Email'])

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
#--------------------------------
if '__main__' == __name__:
    print('*'*50, "\nЗапуск всех тестов по текущей папке по паттерну *Page_Test.py")
    run_all()

    print('*' * 50, "\nВыборочный прогон тестов")
    run_part_test()
