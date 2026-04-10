from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ajax_button_click():
    """
    Нажатие на кнопку и ожидание AJAX-запроса
    Страница: http://uitestingplayground.com/ajax
    """
    # Настройка драйвера Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/ajax")
        driver.maximize_window()
        
        # Ожидание загрузки страницы и кнопки
        wait = WebDriverWait(driver, 10)
        
        # Находим и нажимаем синюю кнопку
        blue_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton"))
        )
        blue_button.click()
        print("Кнопка нажата, ожидание AJAX-ответа...")
        
        # Ожидание появления зеленой плашки с текстом
        # AJAX-запрос может выполняться до 15 секунд
        green_label = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success"))
        )
        
        # Получение текста из зеленой плашки
        label_text = green_label.text
        print(f"Получен текст: {label_text}")
        
        # Проверка соответствия ожидаемому тексту
        expected_text = "Data loaded with AJAX get request."
        assert label_text == expected_text, f"Ожидался текст: {expected_text}, получен: {label_text}"
        
        print("Тест пройден успешно!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    ajax_button_click()