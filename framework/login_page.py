from .page import Page
from appium.webdriver.common.appiumby import AppiumBy


# Reassigning functions in Page class (polymorphism)
class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def find_element(self, el_class):
        # Find login button by class name "login_button" for example
        # Find login and password field
        find_el = self.driver.find_element(AppiumBy.CLASS_NAME, el_class)
        return find_el

    def click_element(self, element):
        # Click a found element
        click = element.click()

