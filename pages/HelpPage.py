from selenium.webdriver import ActionChains

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class HelpPageHelperLocators(BasePageHelper):
    SEARCH_FIELD = (By.XPATH, "//input[@type='search']")
    ACTUAL_TODAY = (By.XPATH, "//a[contains(@href,'segodnya-aktualno')]")
    REGISTRATION = (By.XPATH, "//a[contains(@href,'registraciya')]")
    MY_PROFILE = (By.XPATH, "//a[contains(@href,'moi-profil')]")
    COMMUNICATION = (By.XPATH, "//a[contains(@href,'obshchenie')]")
    PROFILE_ACCESS = (By.XPATH, "//a[contains(@href,'dostup-k-profilu')]")
    SECURITY = (By.XPATH, "//a[contains(@href,'bezopasnost')]")
    GROUP = (By.XPATH, "//a[contains(@href,'gruppy')]")
    PAYED_FUNCTION = (By.XPATH, "//a[contains(@href,'platnye-funkcii')]")
    SPAM = (By.XPATH, "//a[contains(@href,'narusheniya-i-spam')]")
    GAMES_AND_APPS = (By.XPATH, "//a[contains(@href,'igry-i-prilojeniya')]")
    OTHER_SERVICES = (By.XPATH, "//a[contains(@href,'drugie-servisy')]")
    IMPORTANT_INFORMATION = (By.XPATH, "//a[contains(@href,'poleznaya-informaciya')]")
    ADVERTISEMENT_CABINET = (By.XPATH, "//a[contains(@href,'reklamnyi-kabinet')]")


class HelpPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(HelpPageHelperLocators.SEARCH_FIELD)
        self.find_element(HelpPageHelperLocators.ACTUAL_TODAY)
        self.find_element(HelpPageHelperLocators.REGISTRATION)
        self.find_element(HelpPageHelperLocators.MY_PROFILE)
        self.find_element(HelpPageHelperLocators.COMMUNICATION)
        self.find_element(HelpPageHelperLocators.PROFILE_ACCESS)
        self.find_element(HelpPageHelperLocators.SECURITY)
        self.find_element(HelpPageHelperLocators.GROUP)
        self.find_element(HelpPageHelperLocators.PAYED_FUNCTION)
        self.find_element(HelpPageHelperLocators.SPAM)
        self.find_element(HelpPageHelperLocators.GAMES_AND_APPS)
        self.find_element(HelpPageHelperLocators.OTHER_SERVICES)
        self.find_element(HelpPageHelperLocators.IMPORTANT_INFORMATION)
        self.find_element(HelpPageHelperLocators.ADVERTISEMENT_CABINET)

    def scrollToitem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()
