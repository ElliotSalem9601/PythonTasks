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
        # Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")
        
        wait = WebDriverWait(driver, 10)
        
        # Авторизация
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        
        # Добавление товаров в корзину
        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        
        for product_name in products:
            # Находим кнопку Add to cart для каждого товара
            product_locator = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
            add_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, product_locator))
            )
            add_button.click()
            print(f"Товар '{product_name}' добавлен в корзину")
        
        # Переход в корзину
        cart_icon = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon.click()
        
        # Нажать Checkout
        checkout_button = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        
        # Заполнение формы данными
        first_name = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")
        
        first_name.send_keys("Иван")
        last_name.send_keys("Петров")
        postal_code.send_keys("123456")
        
        # Нажать Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        
        # Чтение итоговой стоимости
        total_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        print(f"Итоговая стоимость: {total_text}")
        
        # Извлечение числа из текста (например: "Total: $58.29" -> "$58.29")
        total_amount = total_text.split(":")[1].strip()
        
        # Проверка итоговой суммы
        expected_total = "$58.29"
        assert total_amount == expected_total, \
            f"Expected total: {expected_total}, but got: {total_amount}"
        
        print(f"Тест пройден! Итоговая сумма {total_amount} соответствует ожидаемой {expected_total}")