from features.core.basePage import BasePage
import time


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.menOuterwearShopNowButton = """
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-home").shadowRoot.querySelector("div:nth-child(2) > shop-button > a");
            """

        self.itemMenTechShellFullZip = """
            return document.querySelector("body > shop-app").shadowRoot.querySelector(
            "iron-pages > shop-list").shadowRoot.querySelector(
            "ul > li:nth-child(1) > a > shop-list-item").shadowRoot.querySelector(
            "shop-image").shadowRoot.querySelector("#img")
            """

        self.itemSize = """
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-detail").shadowRoot.querySelector("#sizeSelect");
            """

        self.itemSizeS = """
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-detail").shadowRoot.querySelector("#sizeSelect > option:nth-child(2)")
            """

        self.addToCart = """
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-detail").shadowRoot.querySelector("#content > div > shop-button > button")
            """

        self.checkoutButton = """
            return document.querySelector("body > shop-app").shadowRoot.querySelector("shop-cart-modal").shadowRoot.querySelector(
            "div:nth-child(3) > shop-button:nth-child(2) > a")
            """

    def waitShopNowButtonToBeDisplayed(self):
        self.waitElementToBeDisplayed(self.menOuterwearShopNowButton)

    def clickMenOuterwearShopNowButton(self):
        time.sleep(2)
        element = self.driver.execute_script(self.menOuterwearShopNowButton)
        element.click()

    def clickItemMenTechShellFullZip(self):
        time.sleep(2)
        element = self.driver.execute_script(self.itemMenTechShellFullZip)
        element.click()

    def selectItemSize(self):
        time.sleep(2)
        dropdown = self.driver.execute_script(self.itemSize)
        dropdown.click()
        size = self.driver.execute_script(self.itemSizeS)
        size.click()

    def clickAddToCart(self):
        time.sleep(2)
        element = self.driver.execute_script(self.addToCart)
        element.click()

    def clickCheckoutButton(self):
        time.sleep(2)
        element = self.driver.execute_script(self.checkoutButton)
        element.click()
