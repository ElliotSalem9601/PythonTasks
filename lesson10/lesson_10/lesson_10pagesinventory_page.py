"""Page Object для главной страницы магазина"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.cart_page import CartPage


class InventoryPage:
    """
    Page Object для главной страницы магазина (каталог товаров)
    """

    # Локаторы элементов
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver):
        """
        Инициализация главной страницы
        
        Args:
            driver: WebDriver экземпляр драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _get_item_locator(self, item_name: str) -> tuple:
        """
        Получить локатор для кнопки добавления товара по его имени
        
        Args:
            item_name: Название товара
            
        Returns:
            tuple: Локатор в формате (By, selector)
        """
        return (
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name: str) -> 'InventoryPage':
        """
        Добавить товар в корзину по его названию
        
        Args:
            item_name: Название товара для добавления
            
        Returns:
            InventoryPage: Экземпляр страницы для цепочки вызовов
        """
        add_button = self.wait.until(
            EC.element_to_be_clickable(self._get_item_locator(item_name))
        )
        add_button.click()
        return self

    @allure.step("Добавить рюкзак Sauce Labs Backpack в корзину")
    def add_backpack(self) -> 'InventoryPage':
        """
        Добавить товар Sauce Labs Backpack в корзину
        
        Returns:
            InventoryPage: Экземпляр страницы для цепочки вызовов
        """
        return self.add_item_to_cart("Sauce Labs Backpack")

    @allure.step("Добавить футболку Sauce Labs Bolt T-Shirt в корзину")
    def add_bolt_tshirt(self) -> 'InventoryPage':
        """
        Добавить товар Sauce Labs Bolt T-Shirt в корзину
        
        Returns:
            InventoryPage: Экземпляр страницы для цепочки вызовов
        """
        return self.add_item_to_cart("Sauce Labs Bolt T-Shirt")

    @allure.step("Добавить комбинезон Sauce Labs Onesie в корзину")
    def add_onesie(self) -> 'InventoryPage':
        """
        Добавить товар Sauce Labs Onesie в корзину
        
        Returns:
            InventoryPage: Экземпляр страницы для цепочки вызовов
        """
        return self.add_item_to_cart("Sauce Labs Onesie")

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> CartPage:
        """
        Перейти на страницу корзины
        
        Returns:
            CartPage: Экземпляр страницы корзины
        """
        cart_icon = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart_icon.click()
        return CartPage(self.driver)