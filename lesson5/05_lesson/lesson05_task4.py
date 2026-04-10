from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_test():
    """Тест авторизации на странице http://the-internet.herokuapp.com/login"""
    # Настройка драйвера Firefox
    options = webdriver.FirefoxOptions()
    
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(options=options)
    
    try:
        # Переход на страницу
        driver.get("http://the-internet.herokuapp.com/login")
        driver.maximize_window()
        
        time.sleep(2)
        
        # Ожидание загрузки формы
        wait = WebDriverWait(driver, 10)
        
        # Поиск полей и кнопки
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Ввод логина
        username_field.send_keys("tomsmith")
        print("Введен логин: tomsmith")
        time.sleep(1)
        
        # Ввод пароля
        password_field.send_keys("SuperSecretPassword!")
        print("Введен пароль: SuperSecretPassword!")
        time.sleep(1)
        
        # Нажатие кнопки Login
        login_button.click()
        print("Нажата кнопка Login")
        time.sleep(2)
        
        # Поиск зеленой плашки с сообщением
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        
        # Вывод текста зеленой плашки в консоль
        message_text = success_message.text
        print("\n" + "="*50)
        print("Сообщение об успешной авторизации:")
        print(message_text)
        print("="*50)
        
        time.sleep(2)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрытие браузера
        driver.quit()
        print("\nБраузер закрыт")


if __name__ == "__main__":
    login_test()