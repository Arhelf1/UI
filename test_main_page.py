from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.disk_page import DiskPage


def test_copy_file_to_folder(browser):
    file = 'Файл для копирования'
    folder = 'Files'
    url = 'http://yandex.ru'
    login = 'QASimbirSoft'
    password = 'qwe123QWE!!'
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.auth_user(login, password)
    page.go_to_disk_page()
    disk_page = DiskPage(browser, browser.current_url)
    disk_page.copy_file(file, folder)
    disk_page.open_folder(folder)
    disk_page.delete_files(file)
    assert disk_page.count_files() == 1
    assert disk_page.get_file_name() == file
    disk_page.logout()
