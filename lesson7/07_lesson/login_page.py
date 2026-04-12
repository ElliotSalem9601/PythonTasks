from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы авторизации"""

    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        """Ввести имя пользователя"""
        username_field = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        username_field.send_keys(username)
        return self

    def enter_password(self, password):
        """Ввести пароль"""
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.send_keys(password)
        return self

    def click_login(self):
        """Нажать кнопку входа"""
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        from inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def login(self, username, password):
        """Выполнить авторизацию (комбинированный метод)"""
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()
