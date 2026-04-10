from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object для главной страницы магазина"""

    # Локаторы
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_name):
        """Добавить товар в корзину по имени"""
        item_locator = (
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )
        add_button = self.wait.until(
            EC.element_to_be_clickable(item_locator)
        )
        add_button.click()
        return self

    def add_backpack(self):
        """Добавить рюкзак в корзину"""
        return self.add_item_to_cart("Sauce Labs Backpack")

    def add_bolt_tshirt(self):
        """Добавить футболку в корзину"""
        return self.add_item_to_cart("Sauce Labs Bolt T-Shirt")

    def add_onesie(self):
        """Добавить Onesie в корзину"""
        return self.add_item_to_cart("Sauce Labs Onesie")

    def go_to_cart(self):
        """Перейти в корзину"""
        cart_icon = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart_icon.click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)