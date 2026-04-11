import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class TestSauceDemo:
    """Автотест для интернет-магазина"""

    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации Firefox драйвера"""
        options = webdriver.FirefoxOptions()
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_shopping_cart_total(self, driver):
        """Тест проверки итоговой суммы покупки"""
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)
        
        # Авторизация
        username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = driver.find_element(By.ID, "password")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Добавление товаров в корзину
        items = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }
        
        for item_name, item_id in items.items():
            add_button = wait.until(EC.element_to_be_clickable((By.ID, item_id)))
            add_button.click()
            print(f"Добавлен: {item_name}")
        
        # Переход в корзину
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()
        
        # Checkout
        checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout.click()
        
        # Заполнение формы
        first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name.send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        
        # Continue
        driver.find_element(By.ID, "continue").click()
        
        # Получение итоговой суммы
        total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text
        total_amount = total_text.split("$")[1]
        
        # Проверка
        expected_total = "58.29"
        assert total_amount == expected_total, f"Expected ${expected_total}, got ${total_amount}"
        
        print(f"Итоговая сумма: ${total_amount}")