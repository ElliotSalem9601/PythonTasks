"""Page Object для страницы оформления заказа"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """
    Page Object для страницы оформления заказа
    """

    # Локаторы элементов
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы оформления заказа
        
        Args:
            driver: WebDriver экземпляр драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ввести имя: {first_name}")
    def enter_first_name(self, first_name: str) -> 'CheckoutPage':
        """
        Ввести имя в поле first-name
        
        Args:
            first_name: Имя покупателя
            
        Returns:
            CheckoutPage: Экземпляр страницы для цепочки вызовов
        """
        first_name_field = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_field.send_keys(first_name)
        return self

    @allure.step("Ввести фамилию: {last_name}")
    def enter_last_name(self, last_name: str) -> 'CheckoutPage':
        """
        Ввести фамилию в поле last-name
        
        Args:
            last_name: Фамилия покупателя
            
        Returns:
            CheckoutPage: Экземпляр страницы для цепочки вызовов
        """
        last_name_field = self.driver.find_element(*self.LAST_NAME_INPUT)
        last_name_field.send_keys(last_name)
        return self

    @allure.step("Ввести почтовый индекс: {postal_code}")
    def enter_postal_code(self, postal_code: str) -> 'CheckoutPage':
        """
        Ввести почтовый индекс в поле postal-code
        
        Args:
            postal_code: Почтовый индекс
            
        Returns:
            CheckoutPage: Экземпляр страницы для цепочки вызовов
        """
        postal_code_field = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        postal_code_field.send_keys(postal_code)
        return self

    @allure.step("Заполнить информацию о покупателе")
    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        """
        Заполнить всю информацию о покупателе
        
        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
            
        Returns:
            CheckoutPage: Экземпляр страницы для цепочки вызовов
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> 'CheckoutPage':
        """
        Нажать кнопку продолжения оформления заказа
        
        Returns:
            CheckoutPage: Экземпляр страницы для цепочки вызовов
        """
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()
        return self

    @allure.step("Получить итоговую стоимость заказа")
    def get_total(self) -> str:
        """
        Получить итоговую стоимость заказа
        
        Returns:
            str: Итоговая сумма в формате "$XX.XX"
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        total_text = total_element.text
        # Извлечение суммы (например: "Total: $58.29" -> "$58.29")
        total_amount = total_text.split(":")[1].strip()
        return total_amount