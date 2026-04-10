from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def click_dynamic_button():
    """Клик по синей кнопке на странице http://uitestingplayground.com/dynamicid"""
    # Настройка драйвера Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/dynamicid")
        driver.maximize_window()
        
        time.sleep(2)
        
        # Поиск синей кнопки по тексту или CSS-классу
        # Кнопка имеет класс "btn btn-primary"
        wait = WebDriverWait(driver, 10)
        blue_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
        )
        
        # Альтернативный способ: поиск по тексту
        # blue_button = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Button')]"))
        # )
        
        # Клик по кнопке
        blue_button.click()
        print("Клик по синей кнопке выполнен успешно!")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        driver.quit()


if __name__ == "__main__":
    click_dynamic_button()