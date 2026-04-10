import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class TestDataTypesForm:
    """Автотест для проверки валидации формы"""

    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации Edge драйвера"""
        # Для Edge
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        
        # Для Safari (альтернатива)
        # driver = webdriver.Safari()
        
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_form_validation(self, driver):
        """Тест проверки подсветки полей формы"""
        # Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        wait = WebDriverWait(driver, 10)
        
        # Заполнить форму значениями
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",  # оставить пустым
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        
        for field_id, value in form_data.items():
            field = wait.until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            field.clear()
            if value:  # если значение не пустое
                field.send_keys(value)
        
        # Нажать кнопку Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Проверить, что поле Zip code подсвечено красным
        zip_code_field = driver.find_element(By.ID, "zip-code")
        zip_code_class = zip_code_field.get_attribute("class")
        assert "error" in zip_code_class or "is-invalid" in zip_code_class, \
            "Zip code field should be highlighted in red"
        
        # Проверить, что остальные поля подсвечены зеленым
        success_fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]
        
        for field_id in success_fields:
            field = driver.find_element(By.ID, field_id)
            field_class = field.get_attribute("class")
            assert "success" in field_class or "is-valid" in field_class, \
                f"Field {field_id} should be highlighted in green"
        
        print("Все проверки пройдены успешно!")