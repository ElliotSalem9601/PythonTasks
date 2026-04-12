from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Page Object для страницы корзины"""

    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        """Нажать кнопку Checkout"""
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()
        from checkout_page import CheckoutPage
        return CheckoutPage(self.driver)

    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(cart_items)
