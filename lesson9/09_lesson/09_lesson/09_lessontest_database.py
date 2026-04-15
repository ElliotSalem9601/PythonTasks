"""Автотесты для работы с базой данных"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import Student, Course  # ← импорт из models, а не из model
from database import Base, get_db, init_db, drop_db
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


class TestStudentCRUD:
    """Тесты CRUD операций для студента"""

    def test_create_student(self, db_session, sample_student):
        """Тест добавления студента"""
        db_session.add(sample_student)
        db_session.commit()

        assert sample_student.id is not None
        assert sample_student.first_name == "Иван"
        assert sample_student.email == "ivan@test.com"

        saved_student = db_session.query(Student).filter(
            Student.email == "ivan@test.com"
        ).first()
        assert saved_student is not None

    def test_update_student(self, db_session, sample_student):
        """Тест изменения студента"""
        db_session.add(sample_student)
        db_session.commit()

        sample_student.course = 4
        sample_student.first_name = "Петр"
        db_session.commit()

        updated_student = db_session.query(Student).filter(
            Student.id == sample_student.id
        ).first()
        assert updated_student.course == 4
        assert updated_student.first_name == "Петр"

    def test_delete_student(self, db_session, sample_student):
        """Тест удаления студента"""
        db_session.add(sample_student)
        db_session.commit()
        student_id = sample_student.id

        db_session.delete(sample_student)
        db_session.commit()

        deleted_student = db_session.query(Student).filter(
            Student.id == student_id
        ).first()
        assert deleted_student is None

    def test_soft_delete_student(self, db_session, sample_student):
        """Тест мягкого удаления студента"""
        db_session.add(sample_student)
        db_session.commit()

        sample_student.deleted_at = datetime.now()
        db_session.commit()

        deleted_student = db_session.query(Student).filter(
            Student.id == sample_student.id
        ).first()
        assert deleted_student.deleted_at is not None

        active_students = db_session.query(Student).filter(
            Student.deleted_at.is_(None)
        ).all()
        assert sample_student not in active_students


class TestCourseCRUD:
    """Тесты CRUD операций для курса"""

    def test_create_course(self, db_session, sample_course):
        """Тест добавления курса"""
        db_session.add(sample_course)
        db_session.commit()

        assert sample_course.id is not None
        assert sample_course.title == "Python для начинающих"

    def test_update_course(self, db_session, sample_course):
        """Тест изменения курса"""
        db_session.add(sample_course)
        db_session.commit()

        sample_course.title = "Продвинутый Python"
        sample_course.credits = 6
        db_session.commit()

        updated_course = db_session.query(Course).filter(
            Course.id == sample_course.id
        ).first()
        assert updated_course.title == "Продвинутый Python"
        assert updated_course.credits == 6

    def test_delete_course(self, db_session, sample_course):
        """Тест удаления курса"""
        db_session.add(sample_course)
        db_session.commit()
        course_id = sample_course.id

        db_session.delete(sample_course)
        db_session.commit()

        deleted_course = db_session.query(Course).filter(
            Course.id == course_id
        ).first()
        assert deleted_course is None