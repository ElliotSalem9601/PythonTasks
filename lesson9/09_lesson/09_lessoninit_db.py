"""Скрипт для инициализации базы данных"""

from db_config import init_db, engine
from models import Base

if __name__ == "__main__":
    print("Создание таблиц в базе данных...")
    Base.metadata.create_all(engine)
    print("Таблицы успешно созданы!")