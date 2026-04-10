from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def rename_button():
    """
    Изменение текста на кнопке через поле ввода
    Страница: http://uitestingplayground.com/textinput
    """
    # Настройка драйвера Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/textinput")
        driver.maximize_window()
        
        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)
        
        # Находим поле ввода
        input_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
        )
        
        # Очищаем поле (на всякий случай) и вводим текст "SkyPro"
        input_field.clear()
        input_field.send_keys("SkyPro")
        print("В поле ввода введен текст: SkyPro")
        
        # Находим и нажимаем синюю кнопку
        blue_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
        )
        blue_button.click()
        print("Кнопка нажата")
        
        # Получаем текст кнопки после обновления
        button_text = blue_button.text
        print(f"Текст кнопки после нажатия: {button_text}")
        
        # Проверка соответствия
        expected_text = "SkyPro"
        assert button_text == expected_text, f"Ожидался текст: {expected_text}, получен: {button_text}"
        
        # Выводим в консоль как в задании
        print(f'("{button_text}")')
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    rename_button()