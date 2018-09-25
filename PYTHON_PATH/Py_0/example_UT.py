#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# ������ ������ ������������� ������ unittest
# unittest �������� �������� � Java - JUnit
#--------------------------------
import sys
import unittest
#--------------------------------
class UT_0(unittest.TestCase):
    def setUp(self):
        # �������������, ���������� ����� ������ ������
        pass
    def tearDown(self):
        # ������� � ��������� ���������, ���������� ����� ������� �����, ���� � ����� ����������
        pass
    def test_numbers_3_4(self):
        # ���� ����� ������ �����, � �������� ������ ������ �������������� ����� test
        self.assertEqual(3*4, 12)
    def test_string_a_3(self):
        self.assertEqual('a'*3, 'aaa')
#---------------------------------------
class UT_1(unittest.TestCase):
    def testAssertTrue(self):
        self.assertTrue(True)
    def testAssertFalse(self):
        self.assertFalse(False)
    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.1 - 2.0, places=0)
#---------------------------------------
class NumbCheck(unittest.TestCase):
    # � ������ ����� �������-������, ��� ������������ tests �suite
    def __init__(self, testname, x, y, z=None):
        super(NumbCheck, self).__init__(testname)
        self.x = x
        self.y = y
        self.z = z
    def setUp(self):
        self.x = 0
        self.y = 0
        self.z = 0
    def test_sumNotEq(self):
        sum = self.x + self.y
        self.assertNotEqual(sum, self.z)
    def test_diffMore(self):
        diff = self.x - self.y
        self.assertGreater(diff, self.z)
    def test_Eq(self):
        self.assertEqual(self.x, self.y)
    def tearDown(self):
        # ������� � ��������� ���������, ���������� ����� ������� �����, ���� � ����� ����������
        self.x = 0
        self.y = 0
        self.z = 0
#---------------------------------------
def suite_example():
    suite = unittest.TestSuite()
    suite.addTest(NumbCheck('test_sumNotEq', 22, 5, 10))
    # suite.addTest(unittest.makeSuite(NumbChtest_sumNotEqeck(10, 2, 7)))
    return suite

if '__main__' == __name__:
    # unittest.main() # ��������� ��� unit-�����, ������ ��������� ������ ���� �������� ������ unittest.TestCase

    runner = unittest.TextTestRunner()
    runner.run(suite_example())