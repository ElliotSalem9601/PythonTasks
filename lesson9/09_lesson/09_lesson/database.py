"""Настройка подключения к базе данных"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config import DATABASE_URL
from models import Base  # ← импорт из models, а не из model


# Создание engine
engine = create_engine(DATABASE_URL, echo=True)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Инициализация базы данных (создание таблиц)"""
    Base.metadata.create_all(bind=engine)


def drop_db():
    """Удаление всех таблиц (для очистки)"""
    Base.metadata.drop_all(bind=engine)


def get_db() -> Session:
    """Получение сессии базы данных"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
