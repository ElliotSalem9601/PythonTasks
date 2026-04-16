"""Конфигурация для тестов YouGile API"""

import os
from dotenv import load_dotenv

load_dotenv()

# Базовый URL API (можно изменить для self-hosted версии)
BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://yougile.com/api-v2")

# API ключ - получите в YouGile: Настройки → API ключи
# НУЖНО ЗАМЕНИТЬ НА РЕАЛЬНЫЙ КЛЮЧ ПЕРЕД ЗАПУСКОМ
API_KEY = os.getenv("YOUGILE_API_KEY", "fjEeFp+tcFDkprgqlt5dhtHUIQ4XHbQN-1B1Ud20kXRBEkHGTHH7O-qk2YyuQvUu")

# Проверка наличия ключа
if API_KEY == "fjEeFp+tcFDkprgqlt5dhtHUIQ4XHbQN-1B1Ud20kXRBEkHGTHH7O-qk2YyuQvUu":
    print("WARNING: Используется заглушка API_KEY!")
    print("Получите ключ в YouGile: Настройки → API ключи")
    print("И укажите его в файле .env или config.py")

# Заголовки для запросов (требуются для API YouGile) [citation:3][citation:5]
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# ID для негативных тестов (несуществующий проект)
NON_EXISTENT_ID = "00000000-0000-0000-0000-000000000000"

# Тестовые данные для создания проекта
TEST_PROJECT = {
    "title": "Test Project API",
    "description": "Project created for API testing"
}