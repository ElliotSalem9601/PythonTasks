from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def input_field_test():
    """Тест поля ввода на странице http://the-internet.herokuapp.com/inputs"""
    # Настройка драйвера Firefox
    options = webdriver.FirefoxOptions()
    
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(options=options)
    
    try:
        # Переход на страницу
        driver.get("http://the-internet.herokuapp.com/inputs")
        driver.maximize_window()
        
        time.sleep(2)
        
        # Поиск поля ввода
        wait = WebDriverWait(driver, 10)
        input_field = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        
        # Ввод текста "12345"
        input_field.send_keys("12345")
        print("Введен текст: 12345")
        time.sleep(1)
        
        # Очистка поля
        input_field.clear()
        print("Поле очищено")
        time.sleep(1)
        
        # Ввод текста "54321"
        input_field.send_keys("54321")
        print("Введен текст: 54321")
        time.sleep(2)
        
        # Проверка значения
        value = input_field.get_attribute("value")
        print(f"Текущее значение поля: {value}")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрытие браузера
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    input_field_test()