import time
from behave import *
from features.elements.homePage import HomePage
from features.elements.formPage import FormPage


@given('user access the webpage')
def launchbrowser(context):
    driver = context.driver
    driver.get("https://shop.polymer-project.org/")

@When('select one item and fill the form')
def click_men_outerwear_button(context):
    driver = context.driver
    homePage = HomePage(driver)
    formPage = FormPage(driver)

    homePage.clickMenOuterwearShopNowButton()
    homePage.clickItemMenTechShellFullZip()
    homePage.selectItemSize()
    homePage.clickAddToCart()
    homePage.clickCheckoutButton()

    formPage.insertEmail("automation@test.com")
    formPage.insertPhoneNumber("41996554141")
    formPage.insertShipAddress("Fifth Avenue")
    formPage.insertShipCity("New York")
    formPage.insertShipState("New York")
    formPage.insertShipZip("11122255")
    formPage.insertCardName("Automation")
    formPage.insertCardNumber("111222333444555")
    formPage.insertCardCvv("123")

@Then('click in submit to buy the item')
def selectItem(context):
    driver = context.driver
    formPage = FormPage(driver)

    formPage.clickSubmitButton()
    time.sleep(5) #just to stop in the final screen

    """
    Sorry for the sleeps and few BDD steps, In case I had more time, 
    I would like to create a method in basePage to "waitToElementBeDisplayed".
    """
