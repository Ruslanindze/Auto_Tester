#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# Данный скрипт демонстрирует работу pytest
# pytest является аналогом в Java - TestNG

# способы вызова pytest внутри скрипта
# pytest.main('-v -l example_PyTest.py::test_neg_2 --junitxml=Xml_Reports\\test_neg_2.xml')
# pytest.main('-v -l example_PyTest.py --junitxml=Xml_Reports\\testing_pytest.xml')
#--------------------------------
import pytest
import sys, os
#--------------------------------
def pp(val):
    return val+1

def test_positive():
    assert pp(4) == 5

def test_negative():
    assert pp(5) == 5

def test_neg_2():
    flag = False
    assert True == flag
# --------------------------------
def test():
    x = 3
    y = 4
    assert x == y
# --------------------------------
if '__main__' == __name__:
    # pytest.main('-v -l testing_pytest.py::test --junitxml=Xml_Reports\\test.xml')
    name_script = os.path.basename(sys.argv[0])
    pytest.main(name_script)