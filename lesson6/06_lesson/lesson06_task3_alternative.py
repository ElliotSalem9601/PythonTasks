from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_images_alternative():
    """
    Альтернативная версия с ожиданием конкретного атрибута у картинки
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
        
        # Ожидаем, что у 3-й картинки появится src (не пустой)
        wait = WebDriverWait(driver, 20)
        
        # Ожидаем, что у 3-го изображения атрибут src не пустой
        third_image_src = wait.until(
            lambda d: d.find_elements(By.CSS_SELECTOR, "#image-container img")[2].get_attribute("src")
        )
        
        print(f"src 3-й картинки: {third_image_src}")
        
        # Альтернативный вариант с явным ожиданием загрузки
        # Ждем, пока все изображения не станут видимыми
        images = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#image-container img"))
        )
        
        src_value = images[2].get_attribute("src")
        print(f"\n(Альтернативный способ) src 3-й картинки: {src_value}")
        
    except Exception as e:
        print(f"Ошибка: {e}")
    
    finally:
        driver.quit()


if __name__ == "__main__":
    wait_for_images_alternative()