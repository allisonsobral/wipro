from features.core.basePage import BasePage
import time


class FormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.emailFieldScript = '''
            var element = document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#accountEmail");
            element.value = email;
            '''

        self.phoneNumberFieldScript = '''
            var element = document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#accountPhone")
            element.value = phoneNumber;
            '''

        self.shipAddressFieldScript = '''
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#shipAddress")
            '''

        self.shipCityFieldScript = '''
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#shipCity")
            '''

        self.shipStateFieldScript = '''
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#shipState")
            '''

        self.shipZipFieldScript = '''
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#shipZip")
            '''

        self.cardNameFieldScript = '''
            return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#ccName")
            '''

        self.cardNumberFieldScript = '''
           return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#ccNumber")
           '''

        self.cardCvvFieldScript = '''
           return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#ccCVV")
           '''

        self.submitButton = '''
           return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-checkout").shadowRoot.querySelector("#submitBox > input[type=button]")
           '''

    def insertEmail(self, email):
        time.sleep(2)
        self.driver.execute_script(self.emailFieldScript.replace("email", f'"{email}"'))

    def insertPhoneNumber(self, phoneNumber):
        self.driver.execute_script(self.phoneNumberFieldScript.replace("phoneNumber", f'"{phoneNumber}"'))

    def insertShipAddress(self, shipAddress):
        element = self.driver.execute_script(self.shipAddressFieldScript)
        element.click()
        self.driver.switch_to.active_element.send_keys(shipAddress)

    def insertShipCity(self, shipCity):
        element = self.driver.execute_script(self.shipCityFieldScript)
        element.click()
        self.driver.switch_to.active_element.send_keys(shipCity)
    def insertShipState(self, shipState):
        element = self.driver.execute_script(self.shipStateFieldScript)
        element.click()
        self.driver.switch_to.active_element.send_keys(shipState)

    def insertShipZip(self, shipZip):
        element = self.driver.execute_script(self.shipZipFieldScript)
        element.click()
        self.driver.switch_to.active_element.send_keys(shipZip)

    def insertCardName(self, cardName):
        element = self.driver.execute_script(self.cardNameFieldScript)
        element.click()
        self.driver.switch_to.active_element.send_keys(cardName)

    def insertCardNumber(self, cardNumber):
        element = self.driver.execute_script(self.cardNumberFieldScript)
        element.click()
        self.driver.switch_to.active_element.send_keys(cardNumber)

    def insertCardCvv(self, cardCvv):
        element = self.driver.execute_script(self.cardCvvFieldScript)
        element.click()
        self.driver.switch_to.active_element.send_keys(cardCvv)

    def clickSubmitButton(self):
        time.sleep(2)
        element = self.driver.execute_script(self.submitButton)
        element.click()