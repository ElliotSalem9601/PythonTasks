"""Конфигурация подключения к базе данных"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Параметры подключения к PostgreSQL
# Замените на свои данные!
DB_USER = "myuser"           # Ваше имя пользователя
DB_PASSWORD = "mypassword"   # Ваш пароль
DB_HOST = "localhost"        # Хост (обычно localhost)
DB_PORT = "5432"             # Порт (по умолчанию 5432)
DB_NAME = "mydatabase"       # Имя вашей базы данных

# Строка подключения
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создание engine
engine = create_engine(DATABASE_URL, echo=False)

# Создание всех таблиц (если их нет)
Base.metadata.create_all(engine)

# Создание фабрики сессий
SessionLocal = sessionmaker(bind=engine)


def get_session():
    """Получение сессии базы данных"""
    return SessionLocal()


def init_db():
    """Инициализация базы данных (создание таблиц)"""
    Base.metadata.create_all(engine)
    print("База данных инициализирована")