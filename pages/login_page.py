from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def auth_user(self, login, password):
        self.auth_by_email()
        self.input_login(login)
        self.click_button_login()
        self.input_password(password)
        self.click_button_login()

    def auth_by_email(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON_EMAIL)
        button.click()

    def input_login(self, login):
        input = self.browser.find_element(*LoginPageLocators.EMAIL)
        input.send_keys(login)

    def click_button_login(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON_LOG)
        button.click()

    def input_password(self, password):
        input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input.send_keys(password)
