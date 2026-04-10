from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа"""

    # Локаторы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        """Ввести имя"""
        first_name_field = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_field.send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        """Ввести фамилию"""
        last_name_field = self.driver.find_element(*self.LAST_NAME_INPUT)
        last_name_field.send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        """Ввести почтовый индекс"""
        postal_code_field = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        postal_code_field.send_keys(postal_code)
        return self

    def fill_customer_info(self, first_name, last_name, postal_code):
        """Заполнить информацию о клиенте"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self

    def click_continue(self):
        """Нажать кнопку Continue"""
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()
        return self

    def get_total(self):
        """Получить итоговую стоимость"""
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        total_text = total_element.text
        # Извлечение суммы (например: "Total: $58.29" -> "$58.29")
        total_amount = total_text.split(":")[1].strip()
        return total_amount