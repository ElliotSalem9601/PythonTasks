"""Тесты для калькулятора с Allure отчетами"""

import pytest
import allure
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка работы калькулятора с задержкой")
class TestCalculator:
    """Тесты для калькулятора"""

    @allure.title("Проверка сложения 7 + 8 с задержкой 45 секунд")
    @allure.description("""
    Тест проверяет работу калькулятора с установленной задержкой:
    1. Устанавливается задержка 45 секунд
    2. Выполняется операция 7 + 8
    3. Ожидается результат 15
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("calculator", "smoke", "positive")
    def test_calculator_delay(self, chrome_driver):
        """
        Тест проверки работы калькулятора с задержкой 45 секунд
        
        Args:
            chrome_driver: Фикстура с Chrome WebDriver
        """
        with allure.step("Создание объекта страницы калькулятора"):
            calculator_page = CalculatorPage(chrome_driver)

        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()

        with allure.step("Установка задержки 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Выполнение вычисления 7 + 8"):
            calculator_page.click_button_7()
            calculator_page.click_add()
            calculator_page.click_button_8()
            calculator_page.click_equal()

        with allure.step("Проверка результата вычисления"):
            result = calculator_page.get_result(timeout=50)
            
        with allure.step("Проверка: результат должен быть равен 15"):
            assert result == "15", f"Ожидалось '15', получено '{result}'"

        allure.attach(
            f"Результат вычисления: {result}",
            name="Результат теста",
            attachment_type=allure.attachment_type.TEXT
        )