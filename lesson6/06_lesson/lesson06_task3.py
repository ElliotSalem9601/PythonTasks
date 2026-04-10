from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_images():
    """
    Ожидание загрузки всех картинок и получение src 3-й картинки
    Страница: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
    """
    # Настройка драйвера Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Переход на страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
        driver.maximize_window()
        
        # Ожидание загрузки всех изображений
        wait = WebDriverWait(driver, 20)
        
        # Ожидаем, что все изображения (минимум 3) будут загружены
        # Используем ожидание количества элементов
        images = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img"))
        )
        
        # Проверяем, что загружено минимум 3 изображения
        assert len(images) >= 3, f"Загружено только {len(images)} изображений, ожидалось минимум 3"
        
        # Получаем 3-ю картинку (индекс 2, так как счет с 0)
        third_image = images[2]
        
        # Получаем значение атрибута src
        src_value = third_image.get_attribute("src")
        
        # Выводим значение в консоль
        print(f"Значение атрибута src у 3-й картинки:")
        print(f"{src_value}")
        
        # Дополнительная информация для проверки
        print(f"\nВсего загружено изображений: {len(images)}")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    wait_for_images()