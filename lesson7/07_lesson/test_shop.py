import pytest
from login_page import LoginPage


class TestShop:
    """Тесты для интернет-магазина"""

    def test_shopping_cart_total(self, firefox_driver):
        """Тест проверки итоговой суммы покупки"""
        # Создание объекта страницы авторизации
        login_page = LoginPage(firefox_driver)

        # Шаги теста (только вызовы методов Page Object)
        inventory_page = login_page.open().login("standard_user", "secret_sauce")

        # Добавление товаров в корзину
        inventory_page.add_backpack()
        inventory_page.add_bolt_tshirt()
        inventory_page.add_onesie()

        # Переход в корзину и оформление заказа
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.click_checkout()

        # Заполнение формы
        checkout_page.fill_customer_info("Иван", "Петров", "123456")
        checkout_page.click_continue()

        # Получение итоговой суммы
        total = checkout_page.get_total()

        # Проверка (assert в тесте)
        expected_total = "$58.29"
        assert total == expected_total, \
            f"Expected total: {expected_total}, but got: {total}"

        print(f"Итоговая сумма: {total} соответствует ожидаемой {expected_total}")
