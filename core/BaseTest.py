import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()  # создаем инстанс
    yield driver  # запустили драйвер, дальше браузер сам работаем с ним
    driver.quit()  # после завершения теста закрываем браузер
