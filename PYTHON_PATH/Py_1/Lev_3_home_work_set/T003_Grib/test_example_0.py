from selenium import webdriver
import unittest
import sys
sys.path.append(r'd:\WORK_MC_21\Tester\Auto_Tester\PYTHON_PATH\Commons')
import DriverManager as DM
#----------------------------------------------
class ExampleTestCase(unittest.TestCase):
    # capabilities = None
    Browser = None
    def setUp(self):
        # self.driver = webdriver.Remote(desired_capabilities=self.capabilities)
        self.driver = DM.Driver_Manager(self.Browser).driver
        print(self.driver.desired_capabilities)

    def test_example(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    # ExampleTestCase.Browser = "chrome"
    # ExampleTestCase.capabilities = {
    #     "browserName": sys.argv[1],
    #     "platform": sys.argv[2],
    # }
    # unittest.main()

    ExampleTestCase.Browser = sys.argv[1]
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)
    result_FF = runner.run(loader.loadTestsFromTestCase(ExampleTestCase))