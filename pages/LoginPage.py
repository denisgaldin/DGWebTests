from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

from pages.RecoveryPage import RecoveryPageLocators


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, '//form//button[.//span[text()="Войти"]]')
    LOGIN_QR_BUTTON = (By.XPATH, '//button[contains(., "QR-коду")]')
    RECOVERY_BUTTON = (By.XPATH, '//button[contains(., "Не получается войти")]')
    REGISTER_BUTTON = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    MAIL_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    LOGIN_QR_ELEMENT = (By.XPATH, '//*[starts-with(@id, "qrCode-")]')
    SERVICE_VK = (By.ID, "hook_Block_Header")
    SEARCH = (By.ID, "toolbar_search")
    ERROR_TEXT = (By.XPATH, '//span[contains(text(), "Введите логин") or contains(text(), "Введите пароль")]')
    GO_BACK_BUTTON = (By.XPATH, "//button[.//span[text()='Отмена']]")


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_BUTTON)
        self.find_element(LoginPageLocators.RECOVERY_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_ELEMENT)
        self.find_element(LoginPageLocators.SERVICE_VK)
        self.find_element(LoginPageLocators.SEARCH)

    @allure.step("Нажимаем на кнопку войти")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Вводим логин')
    def enter_login(self, login_text):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login_text)
        self.attach_screenshot()

    @allure.step('Вводим пароль')
    def enter_password(self, password_text):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password_text)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVERY_BUTTON).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()
