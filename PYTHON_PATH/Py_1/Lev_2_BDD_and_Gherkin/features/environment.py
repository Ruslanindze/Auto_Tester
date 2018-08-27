# -- FILE features/environment.py
# CONTAINS: Browser fixture setup and tesaradown
from behave import fixture, use_fixture
from selenium.webdriver import Firefox
import time
#---------------------------------------
PATH_DRIVER_FIREFOX = "d:\WORK_MC_21\Tester\Auto_Tester\geckodriver.exe"
#---------------------------------------
@fixture
def browser_firefox(context):
    # --BEHAVE_FIXTURE:Similar to @contextlib.contextmanager
    context.browser = Firefox(executable_path=PATH_DRIVER_FIREFOX)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    time.sleep(3)
    context.browser.quit()

def before_all(context):
    use_fixture(browser_firefox, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook