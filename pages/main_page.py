from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        """go to authorization page"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_disk_page(self):
        """go to yandex disk page"""
        link = self.browser.find_element(*BasePageLocators.DISK_LINK)
        link.click()
