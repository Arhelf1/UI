from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR,
                  '.desk-notif-card__login-new-item-title.desk-notif-card__login-new-item-title')
    DISK_LINK = (By.CSS_SELECTOR,
                 '[data-statlog="notifications.mail.login.disk"]')


class LoginPageLocators:
    BUTTON_EMAIL = (By.CSS_SELECTOR, '[data-type="login"]')
    EMAIL = (By.ID, 'passp-field-login')
    PASSWORD = (By.ID, 'passp-field-passwd')
    BUTTON_LOG = (By.ID, 'passp:sign-in')


class DiskPageLocators:
    FILE_FOLDER = (By.CSS_SELECTOR)
    BUTTON_TO_COPY_TOP_MENU = (By.CSS_SELECTOR, '[aria-label="Копировать"]')
    BUTTON_COPY_IN_COPY_DIALOG = (By.CSS_SELECTOR, '.Button2.Button2_view_action.Button2_size_m.confirmation-dialog_'
                                  '_button.confirmation-dialog__button_submit ')
    BUTTON_ALL = (By.CSS_SELECTOR, '[aria-label="Ещё"]')
    BUTTON_COPY_MENU_ALL = (By.CSS_SELECTOR, '.Menu-Item.Menu-Item_type_menuitem.groupable-buttons_'
                            '_menu-button.groupable-buttons__menu-button_action_copy ')
    FILES_ALL = (By.CSS_SELECTOR, '.listing-item.listing-item_theme_tile.listing-item_'
                                  'size_m.listing-item_type_file.js-prevent-deselect')
    FILES_NAMES_ALL = (
        By.CSS_SELECTOR, '.listing-item__title.listing-item__title_overflow_clamp')
    BUTTON_DELETE = (By.CSS_SELECTOR, '[aria-label="Удалить"]')
    ACCOUNT = (By.CSS_SELECTOR, '[aria-label="Аккаунт"]')
    BUTTON_EXIT = (By.CSS_SELECTOR, '[aria-label="Выйти из аккаунта"]')
    ALERT = (By.CSS_SELECTOR, '.operations-progress')


class Settings:
    FILE = 'Файл для копирования'
    FOLDER = 'Files'
    URL = 'http://yandex.ru'
    LOGIN = 'QASimbirSoft'
    PASSWORD = 'qwe123QWE!!'
