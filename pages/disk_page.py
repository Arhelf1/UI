from .base_page import BasePage
from .locators import DiskPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class DiskPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(DiskPage, self).__init__(*args, **kwargs)

    def click_button_copy_menu_all(self):
        button_copy_all = self.browser.find_element(
            *DiskPageLocators.BUTTON_COPY_MENU_ALL)
        button_copy_all.click()

    def click_button_menu_all(self):
        button_all = self.browser.find_element(*DiskPageLocators.BUTTON_ALL)
        button_all.click()

    def click_button_copy_in_menu(self):
        button = self.browser.find_element(
            *DiskPageLocators.BUTTON_COPY_IN_COPY_DIALOG)
        button.click()

    def click_button_to_copy(self):
        button = self.browser.find_element(
            *DiskPageLocators.BUTTON_TO_COPY_TOP_MENU)
        if button.is_enabled() and button.is_displayed():
            button.click()
        else:
            self.click_button_menu_all()
            self.click_button_copy_menu_all()

    def click_file(self, file_name):
        while not self.is_element_present(DiskPageLocators.FILE_FOLDER, f'[aria-label^="{file_name}"]'):
            self.browser.implicitly_wait(1)
        file_to_click = self.browser.find_element(
            DiskPageLocators.FILE_FOLDER, f'[aria-label^="{file_name}"]')
        file_to_click.click()

    def click_to_folder_in_menu(self, folder_name):
        folder = self.browser.find_element(
            DiskPageLocators.FILE_FOLDER, f'[title="{folder_name}"]')
        folder.click()

    def copy_file(self, file_name, folder_name):
        BasePage.go_to_new_window(self)
        self.click_file(file_name)
        self.click_button_to_copy()
        self.click_to_folder_in_menu(folder_name)
        self.click_button_copy_in_menu()

    def count_files(self):
        files = self.browser.find_elements(*DiskPageLocators.FILES_ALL)
        return len(files)

    def delete_files(self, file_name):
        while not self.is_element_present(DiskPageLocators.FILE_FOLDER, f'[aria-label^="{file_name}"]'):
            self.browser.implicitly_wait(1)
        count = self.count_files()
        if count > 1:
            names = self.get_files_names()
            for name in names:
                if name != file_name:
                    self.delete_one_file(name)

    def delete_one_file(self, file_name):
        self.click_file(file_name)
        button_delete = self.browser.find_element(
            *DiskPageLocators.BUTTON_DELETE)
        button_delete.click()
        self.browser.implicitly_wait(1)

    def double_click_folder_on_disk(self, folder_name):
        folder_to_click = self.browser.find_element(
            DiskPageLocators.FILE_FOLDER, f'[aria-label="{folder_name}"]')
        action = ActionChains(self.browser)
        action.double_click(folder_to_click).perform()

    def get_file_name(self):
        name = self.browser.find_element(*DiskPageLocators.FILES_NAMES_ALL)
        text = name.get_attribute("aria-label").split('.')[0]
        return text

    def get_files_names(self):
        files = self.browser.find_elements(*DiskPageLocators.FILES_NAMES_ALL)
        texts = [name.get_attribute("aria-label").split('.')[0]
                 for name in files]
        return texts

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open_folder(self, folder_name):
        self.double_click_folder_on_disk(folder_name)

    def logout(self):
        while self.is_element_present(*DiskPageLocators.ALERT):
            self.browser.implicitly_wait(1)
        account = self.browser.find_element(*DiskPageLocators.ACCOUNT)
        account.click()
        button_exit = self.browser.find_element(*DiskPageLocators.BUTTON_EXIT)
        button_exit.click()
