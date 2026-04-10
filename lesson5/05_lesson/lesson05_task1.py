from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def click_blue_button():
    """Клик по синей кнопке на странице http://uitestingplayground.com/classattr"""
    # Настройка драйвера Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    # Инициализация драйвера
    driver = webdriver.Chrome(options=options)
    
    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/classattr")
        driver.maximize_window()
        
        # Ожидание загрузки страницы
        time.sleep(2)
        
        # Поиск синей кнопки по CSS-классу
        # Синяя кнопка имеет класс "btn-primary"
        wait = WebDriverWait(driver, 10)
        blue_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
        )
        
        # Клик по кнопке
        blue_button.click()
        print("Клик по синей кнопке выполнен успешно!")
        
        # Небольшая пауза для отображения результата
        time.sleep(2)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    click_blue_button()