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
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_calculator_delay(self, driver):
        """Тест калькулятора с задержкой 45 секунд"""
        # Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        wait = WebDriverWait(driver, 10)
        
        # В поле ввода #delay ввести значение 45
        delay_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_field.clear()
        delay_field.send_keys("45")
        
        # Нажать кнопки: 7 + 8 =
        buttons = [
            "7", "add", "8", "equal"
        ]
        
        for button_id in buttons:
            button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"#btn-{button_id}"))
            )
            button.click()
        
        # Ожидание результата с учетом задержки 45 секунд
        # Используем WebDriverWait с таймаутом 50 секунд (45 + запас)
        result_wait = WebDriverWait(driver, 50)
        result_element = result_wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        
        # Проверка результата
        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        result_text = screen.text
        assert result_text == "15", f"Expected '15', but got '{result_text}'"
        
        print(f"Результат: {result_text} (получен через 45 секунд)")