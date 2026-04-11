import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
import os


class TestDataTypesForm:
    """Автотест для проверки валидации формы"""

    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации Edge драйвера"""
        edge_driver_path = r"C:\Users\ElliotSalem\OneDrive\Рабочий стол\lesson6k\webdrivers\msedgedriver.exe"
        
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        service = EdgeService(executable_path=edge_driver_path)
        driver = webdriver.Edge(service=service, options=options)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_form_validation(self, driver):
        """Тест проверки подсветки полей формы"""
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait = WebDriverWait(driver, 10)
        
        # Заполнение формы
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        
        for field_id, value in fields.items():
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field.clear()
            if value:
                field.send_keys(value)
        
        # Нажатие кнопки Submit
        submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        
        # Проверка подсветки полей
        # Красный цвет для Zip code (класс alert-danger или is-invalid)
        zip_field = driver.find_element(By.ID, "zip-code")
        zip_classes = zip_field.get_attribute("class")
        assert "alert-danger" in zip_classes or "is-invalid" in zip_classes or "error" in zip_classes, \
            "Zip code field should be red"
        
        # Зеленый цвет для остальных полей (класс alert-success или is-valid)
        success_fields = ["first-name", "last-name", "address", "e-mail", 
                         "phone", "city", "country", "job-position", "company"]
        
        for field_id in success_fields:
            field = driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")
            assert "alert-success" in field_classes or "is-valid" in field_classes or "success" in field_classes, \
                f"Field {field_id} should be green"
        
        print("Все проверки пройдены успешно!")