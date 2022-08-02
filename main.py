from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.disk_page import DiskPage
from pages.locators import Settings as S


def test_copy_file_to_folder(browser):
    page = MainPage(browser, S.URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.auth_user(S.LOGIN, S.PASSWORD)
    page.go_to_disk_page()
    disk_page = DiskPage(browser, browser.current_url)
    disk_page.copy_file(S.FILE, S.FOLDER)
    disk_page.open_folder(S.FOLDER)
    disk_page.delete_files(S.FILE)
    assert disk_page.count_files() == 1
    assert disk_page.get_file_name() == S.FILE
    disk_page.logout()
