"""Page Object для страницы авторизации"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.inventory_page import InventoryPage


class LoginPage:
    """
    Page Object для страницы авторизации
    URL: https://www.saucedemo.com/
    """

    # Локаторы элементов
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы авторизации
        
        Args:
            driver: WebDriver экземпляр драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        """
        Открыть страницу авторизации
        
        Returns:
            LoginPage: Экземпляр страницы для цепочки вызовов
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> 'LoginPage':
        """
        Ввести имя пользователя в поле username
        
        Args:
            username: Имя пользователя для авторизации
            
        Returns:
            LoginPage: Экземпляр страницы для цепочки вызовов
        """
        username_field = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        username_field.send_keys(username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> 'LoginPage':
        """
        Ввести пароль в поле password
        
        Args:
            password: Пароль для авторизации
            
        Returns:
            LoginPage: Экземпляр страницы для цепочки вызовов
        """
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.send_keys(password)
        return self

    @allure.step("Нажать кнопку входа Login")
    def click_login(self) -> InventoryPage:
        """
        Нажать кнопку входа в систему
        
        Returns:
            InventoryPage: Экземпляр страницы каталога товаров
        """
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        return InventoryPage(self.driver)

    @allure.step("Выполнить авторизацию пользователем {username}")
    def login(self, username: str, password: str) -> InventoryPage:
        """
        Выполнить полную авторизацию (комбинированный метод)
        
        Args:
            username: Имя пользователя
            password: Пароль
            
        Returns:
            InventoryPage: Экземпляр страницы каталога товаров
        """
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()