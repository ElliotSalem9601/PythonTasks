from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы калькулятора"""

    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")
    
    # Исправленные локаторы для кнопок (используем точные селекторы)
    BTN_7 = (By.XPATH, "//span[text()='7']")
    BTN_8 = (By.XPATH, "//span[text()='8']")
    BTN_ADD = (By.XPATH, "//span[text()='+']")
    BTN_EQUAL = (By.XPATH, "//span[text()='=']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открыть страницу калькулятора"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds):
        """Установить задержку в секундах"""
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    def click_button_7(self):
        """Нажать кнопку 7"""
        button = self.wait.until(
            EC.element_to_be_clickable(self.BTN_7)
        )
        button.click()
        return self

    def click_button_8(self):
        """Нажать кнопку 8"""
        button = self.wait.until(
            EC.element_to_be_clickable(self.BTN_8)
        )
        button.click()
        return self

    def click_add(self):
        """Нажать кнопку +"""
        button = self.wait.until(
            EC.element_to_be_clickable(self.BTN_ADD)
        )
        button.click()
        return self

    def click_equal(self):
        """Нажать кнопку ="""
        button = self.wait.until(
            EC.element_to_be_clickable(self.BTN_EQUAL)
        )
        button.click()
        return self

    def get_result(self, timeout=50):
        """Получить результат с учетом задержки"""
        result_wait = WebDriverWait(self.driver, timeout)
        result_wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, "15")
        )
        screen = self.driver.find_element(*self.SCREEN)
        return screen.text
