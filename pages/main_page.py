from .base_page import BasePage
from selenium.webdriver.common.by import By
import time


class MainPage(BasePage):

    def should_be_login_link(self):
        time.sleep(1)
