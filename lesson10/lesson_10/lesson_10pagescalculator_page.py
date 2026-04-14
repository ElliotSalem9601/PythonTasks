"""Page Object для страницы калькулятора"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """
    Page Object для страницы калькулятора
    URL: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    """

    # Локаторы элементов
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")
    BTN_7 = (By.XPATH, "//span[text()='7']")
    BTN_8 = (By.XPATH, "//span[text()='8']")
    BTN_ADD = (By.XPATH, "//span[text()='+']")
    BTN_EQUAL = (By.XPATH, "//span[text()='=']")

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы калькулятора
        
        Args:
            driver: WebDriver экземпляр драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> 'CalculatorPage':
        """
        Открыть страницу калькулятора
        
        Returns:
            CalculatorPage: Экземпляр страницы для цепочки вызовов
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> 'CalculatorPage':
        """
        Установить задержку перед вычислением
        
        Args:
            seconds: Количество секунд задержки
            
        Returns:
            CalculatorPage: Экземпляр страницы для цепочки вызовов
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    @allure.step("Нажать кнопку 7")
    def click_button_7(self) -> 'CalculatorPage':
        """
        Нажать кнопку с цифрой 7
        
        Returns:
            CalculatorPage: Экземпляр страницы для цепочки вызовов
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BTN_7)
        )
        button.click()
        return self

    @allure.step("Нажать кнопку 8")
    def click_button_8(self) -> 'CalculatorPage':
        """
        Нажать кнопку с цифрой 8
        
        Returns:
            CalculatorPage: Экземпляр страницы для цепочки вызовов
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BTN_8)
        )
        button.click()
        return self

    @allure.step("Нажать кнопку сложения (+)")
    def click_add(self) -> 'CalculatorPage':
        """
        Нажать кнопку операции сложения
        
        Returns:
            CalculatorPage: Экземпляр страницы для цепочки вызовов
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BTN_ADD)
        )
        button.click()
        return self

    @allure.step("Нажать кнопку равно (=)")
    def click_equal(self) -> 'CalculatorPage':
        """
        Нажать кнопку равно для получения результата
        
        Returns:
            CalculatorPage: Экземпляр страницы для цепочки вызовов
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.BTN_EQUAL)
        )
        button.click()
        return self

    @allure.step("Получить результат вычисления")
    def get_result(self, timeout: int = 50) -> str:
        """
        Получить результат вычисления с учетом задержки
        
        Args:
            timeout: Максимальное время ожидания результата в секундах
            
        Returns:
            str: Текст результата на экране калькулятора
        """
        result_wait = WebDriverWait(self.driver, timeout)
        result_wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, "15")
        )
        screen = self.driver.find_element(*self.SCREEN)
        return screen.text