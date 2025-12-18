from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON = (By.XPATH, '//form//button[.//span[text()="Войти"]]')
    LOGIN_QR_BUTTON = (By.XPATH, '//button[contains(., "QR-коду")]')
    PROBLEM_LOGIN_LINK = (By.XPATH, '//button[contains(., "Не получается войти")]')
    REGISTER_BUTTON = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    MAIL_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    LOGIN_QR_ELEMENT = (By.XPATH, '//*[starts-with(@id, "qrCode-")]')
    SERVICE_VK = (By.ID, "hook_Block_Header")
    SEARCH = (By.ID, "toolbar_search")
    ERROR_TEXT = (By.XPATH, '//span[contains(text(), "Введите логин") or contains(text(), "Введите пароль")]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_BUTTON)
        self.find_element(LoginPageLocators.PROBLEM_LOGIN_LINK)
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
        login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(login_text)
