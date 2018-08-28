from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys, unittest, time

class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://172.20.1.150:4444/wd/hub',
            desired_capabilities={
            "browserName": "chrome",
            "platform": "WINDOWS",
        })
        # self.driver = webdriver.Remote(command_executor='http://172.20.1.150:4444/wd/hub',
        #                           desired_capabilities=DesiredCapabilities.CHROME)
        # self.driver.start_client()

    def test_example(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":


    unittest.main()
