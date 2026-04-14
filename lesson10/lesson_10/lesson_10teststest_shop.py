"""Тесты для интернет-магазина с Allure отчетами"""

import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("Интернет-магазин Sauce Demo")
@allure.story("Проверка оформления заказа")
class TestShop:
    """Тесты для интернет-магазина"""

    @allure.title("Проверка итоговой суммы покупки трех товаров")
    @allure.description("""
    Тест проверяет корректность расчета итоговой суммы:
    1. Авторизация пользователем standard_user
    2. Добавление трех товаров в корзину
    3. Оформление заказа
    4. Проверка итоговой суммы $58.29
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("shop", "smoke", "positive", "e2e")
    def test_shopping_cart_total(self, firefox_driver):
        """
        Тест проверки итоговой суммы покупки
        
        Args:
            firefox_driver: Фикстура с Firefox WebDriver
        """
        with allure.step("Создание объекта страницы авторизации"):
            login_page = LoginPage(firefox_driver)

        with allure.step("Открытие страницы авторизации"):
            login_page.open()

        with allure.step("Авторизация пользователем standard_user"):
            inventory_page = login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            inventory_page.add_backpack()
            allure.attach("Добавлен: Sauce Labs Backpack", "Товар 1", allure.attachment_type.TEXT)
            
            inventory_page.add_bolt_tshirt()
            allure.attach("Добавлен: Sauce Labs Bolt T-Shirt", "Товар 2", allure.attachment_type.TEXT)
            
            inventory_page.add_onesie()
            allure.attach("Добавлен: Sauce Labs Onesie", "Товар 3", allure.attachment_type.TEXT)

        with allure.step("Переход в корзину"):
            cart_page = inventory_page.go_to_cart()

        with allure.step("Нажатие кнопки Checkout"):
            checkout_page = cart_page.click_checkout()

        with allure.step("Заполнение формы данными покупателя"):
            checkout_page.fill_customer_info("Иван", "Петров", "123456")

        with allure.step("Нажатие кнопки Continue"):
            checkout_page.click_continue()

        with allure.step("Получение итоговой стоимости"):
            total = checkout_page.get_total()

        with allure.step(f"Проверка: итоговая сумма должна быть $58.29 (получено {total})"):
            expected_total = "$58.29"
            assert total == expected_total, \
                f"Ожидаемая сумма: {expected_total}, получена: {total}"

        allure.attach(
            f"Итоговая сумма: {total}",
            name="Результат проверки",
            attachment_type=allure.attachment_type.TEXT
        )