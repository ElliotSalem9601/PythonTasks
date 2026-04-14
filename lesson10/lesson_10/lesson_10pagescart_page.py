"""Page Object для страницы корзины"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.checkout_page import CheckoutPage


class CartPage:
    """
    Page Object для страницы корзины
    """

    # Локаторы элементов
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы корзины
        
        Args:
            driver: WebDriver экземпляр драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку Checkout (оформление заказа)")
    def click_checkout(self) -> CheckoutPage:
        """
        Нажать кнопку перехода к оформлению заказа
        
        Returns:
            CheckoutPage: Экземпляр страницы оформления заказа
        """
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()
        return CheckoutPage(self.driver)