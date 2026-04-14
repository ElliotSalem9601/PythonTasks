import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestSlowCalculator:
    """Автотест для калькулятора с задержкой"""

    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации Chrome драйвера"""
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-blink-features=AutomationControlled')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_calculator_delay(self, driver):
        """Тест калькулятора с задержкой 45 секунд"""
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        wait = WebDriverWait(driver, 10)
        
        # Установка задержки
        delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys("45")
        
        # Нажатие кнопок
        buttons = ["7", "8", "add", "equal"]
        for btn in buttons:
            button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{btn}']")))
            button.click()
        
        # Ожидание результата
        result_wait = WebDriverWait(driver, 50)
        screen = result_wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen"))
        )
        
        result_text = screen.text
        assert result_text == "15", f"Expected '15', got '{result_text}'"
        
        print(f"Результат: {result_text}")