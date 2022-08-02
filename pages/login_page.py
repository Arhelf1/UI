from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def auth_user(self, login, password):
        self.click_auth_by_email()
        self.set_value(LoginPageLocators.EMAIL, login)
        self.click_button_login()
        self.set_value(LoginPageLocators.PASSWORD, password)
        self.click_button_login()

    def click_auth_by_email(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON_EMAIL)
        button.click()

    def click_button_login(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON_LOG)
        button.click()
