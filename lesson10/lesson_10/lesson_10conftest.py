"""Фикстуры для тестов"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure


@pytest.fixture
def chrome_driver():
    """
    Фикстура для Chrome драйвера
    
    Returns:
        WebDriver: Экземпляр Chrome WebDriver
    """
    with allure.step("Инициализация Chrome драйвера"):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-blink-features=AutomationControlled')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        
    yield driver
    
    with allure.step("Закрытие Chrome драйвера"):
        driver.quit()


@pytest.fixture
def firefox_driver():
    """
    Фикстура для Firefox драйвера
    
    Returns:
        WebDriver: Экземпляр Firefox WebDriver
    """
    with allure.step("Инициализация Firefox драйвера"):
        options = webdriver.FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        
    yield driver
    
    with allure.step("Закрытие Firefox драйвера"):
        driver.quit()