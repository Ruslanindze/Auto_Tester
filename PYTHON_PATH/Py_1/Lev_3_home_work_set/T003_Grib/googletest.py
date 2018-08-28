import selenium as Sel
import unittest, time ,re

class googletestvase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = Sel("http://172.20.1.150", 4444, "*firefox", "http://www.google.com/")
        self.selenium.start()
    #----------------------------
    def test_googletestcase(self):
        sel = self.selenium
        sel.open("/")
        sel.click("id=lst-ib")
        sel.type("id=lst-ib", "test")
        sel.type("id=lst-ib", "another test")
        sel.click()
    # ----------------------------
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
# ----------------------------
if __name__ == "__main__":
    unittest.main()