from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys, unittest, time

class ExampleTestCase(unittest.TestCase):
    capabilities = None
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://172.20.1.150:4444/wd/hub',\
                                       desired_capabilities=self.capabilities)

    def test_example(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    allowed_browsers = ['chrome', 'firefox', 'ie']
    argv_browser = sys.argv[1].lower()

    if argv_browser == 'ie':
        ExampleTestCase.capabilities = DesiredCapabilities.INTERNETEXPLORER
    elif argv_browser in allowed_browsers:
        ExampleTestCase.capabilities = {
            "browserName": argv_browser,
            "platform": "WINDOWS",
        }

    # unittest.main() # не запускается, только через suite

    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(loader.loadTestsFromTestCase(ExampleTestCase))