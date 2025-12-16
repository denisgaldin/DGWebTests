from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, '//form//button[.//span[text()="Войти"]]')
    LOGIN_QR_BUTTON = (By.XPATH, '//button[contains(., "QR-коду")]')
    PROBLEM_LOGIN_LINK = (By.XPATH, '//button[contains(., "Не получается войти")]')
    REGISTER_BUTTON = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    VK_BUTTON = (By.XPATH, '//a[contains(@href, "vk.com") or contains(@class, "vk")]')
    MAIL_BUTTON = (By.XPATH, '//a[contains(@href, "mail.ru") or contains(@class, "mail")]')
    YANDEX_BUTTON = (By.XPATH, '//a[contains(@href, "ya.ru") or contains(@class, "ya.ru")]')
    LOGIN_QR_ELEMENT = (By.XPATH, '//*[starts-with(@id, "qrCode-")]')
    SERVICE_VK = (By.ID, "hook_Block_Header")
    SEARCH = (By.ID, "toolbar_search")


class LoginPageHelper(BasePage):
    pass
