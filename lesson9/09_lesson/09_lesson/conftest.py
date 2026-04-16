"""Фикстуры для тестов базы данных"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Course
from database import Base
from config import DATABASE_URL


# Используем отдельную тестовую базу данных
TEST_DATABASE_URL = DATABASE_URL.replace("mydatabase", "test_database")


@pytest.fixture(scope="session")
def test_engine():
    """Фикстура для тестового engine"""
    engine = create_engine(TEST_DATABASE_URL, echo=True)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture
def db_session(test_engine):
    """Фикстура для сессии базы данных"""
    connection = test_engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def sample_student():
    """Фикстура с примером студента"""
    return Student(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com",
        course=3,
        is_active=True
    )


@pytest.fixture
def sample_course():
    """Фикстура с примером курса"""
    return Course(
        title="Python для начинающих",
        description="Базовый курс Python",
        credits=5
    )