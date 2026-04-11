from calculator_page import CalculatorPage
from cart_page import CartPage


class TestCalculator:
    """Тесты для калькулятора"""

    def test_calculator_delay(self, chrome_driver):
        """Тест проверки работы калькулятора с задержкой"""
        # Создание объекта страницы
        calculator_page = CalculatorPage(chrome_driver)

        # Шаги теста (только вызовы методов Page Object)
        calculator_page.open()
        calculator_page.set_delay(45)
        calculator_page.click_button_7()
        calculator_page.click_add()
        calculator_page.click_button_8()
        calculator_page.click_equal()

        # Проверка результата (assert в тесте)
        result = calculator_page.get_result(timeout=50)
        assert result == "15", f"Expected '15', but got '{result}'"

        print(f"Результат: {result} (получен через 45 секунд)")
