from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_text_from_element(self, element: WebElement) -> str:
        return element.text
    def sendKeysToElement(self, element, text):
        elementLocator = self.driver.find_element(*element)
        elementLocator.clear()
        elementLocator.send_keys(text)

    def isElementDisplayed(self, locator):
        element = self.driver.find_element(*locator)
        assert element.is_displayed(), f"Element {locator} is not visible."

    def waitElementToBeDisplayed(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutError(f"Element not displayed after {timeout} seconds.")

    def waitElementToNotBeDisplayed(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutError(f"Element is still visible after {timeout} seconds.")
