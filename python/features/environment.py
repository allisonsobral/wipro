from selenium import webdriver
from behave import fixture, use_fixture

@fixture
def setup_driver(context):
    driver = webdriver.Chrome()
    driver.maximize_window()
    context.driver = driver
    yield context.driver
    driver.quit()

def before_all(context):
    use_fixture(setup_driver, context)
