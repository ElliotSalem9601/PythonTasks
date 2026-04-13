import pytest
from pages.calculator_page import CalculatorPage


class TestCalculator:
    """Тесты для калькулятора"""

    def test_calculator_delay(self, chrome_driver):
        """Тест проверки работы калькулятора с задержкой"""
        calculator_page = CalculatorPage(chrome_driver)
        
        calculator_page.open()
        calculator_page.set_delay(45)
        
        
        import time
        calculator_page.click_button_7()
        time.sleep(0.5)
        calculator_page.click_add()
        time.sleep(0.5)
        calculator_page.click_button_8()
        time.sleep(0.5)
        calculator_page.click_equal()
        
        result = calculator_page.get_result(timeout=50)
        assert result == "15", f"Expected '15', but got '{result}'"
        
        print(f"Результат: {result}")
