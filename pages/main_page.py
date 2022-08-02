from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_disk_page(self):
        link = self.browser.find_element(*BasePageLocators.DISK_LINK)
        link.click()
