"""Автотесты для операций с базой данных"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Course, Enrollment, Base
from db_config import DATABASE_URL, get_session


class TestDatabaseOperations:
    """Тесты для CRUD операций с БД"""

    @pytest.fixture
    def session(self):
        """Фикстура для сессии БД с очисткой после тестов"""
        # Создаем тестовую БД (можно использовать отдельную для тестов)
        test_engine = create_engine(DATABASE_URL, echo=False)
        Base.metadata.create_all(test_engine)
        TestSession = sessionmaker(bind=test_engine)
        session = TestSession()

        yield session

        # Очистка после тестов
        session.query(Student).delete()
        session.query(Course).delete()
        session.query(Enrollment).delete()
        session.commit()
        session.close()

    # ========== Тесты для добавления (CREATE) ==========

    def test_create_student_positive(self, session):
        """Позитивный тест: добавление нового студента"""
        student = Student(
            first_name="Иван",
            last_name="Тестов",
            email=f"ivan.test_{id(session)}@example.com",
            group_name="A-101"
        )

        session.add(student)
        session.commit()

        # Проверка
        assert student.id is not None
        saved_student = session.query(Student).filter_by(id=student.id).first()
        assert saved_student is not None
        assert saved_student.first_name == "Иван"
        assert saved_student.last_name == "Тестов"
        assert saved_student.group_name == "A-101"

    def test_create_student_negative_duplicate_email(self, session):
        """Негативный тест: добавление студента с существующим email"""
        # Создаем первого студента
        student1 = Student(
            first_name="Петр",
            last_name="Первый",
            email="duplicate@example.com",
            group_name="B-202"
        )
        session.add(student1)
        session.commit()

        # Пытаемся создать второго с тем же email
        student2 = Student(
            first_name="Иван",
            last_name="Второй",
            email="duplicate@example.com",  # Тот же email
            group_name="C-303"
        )
        session.add(student2)

        # Должна быть ошибка нарушения уникальности
        with pytest.raises(Exception):
            session.commit()

        session.rollback()

    def test_create_student_negative_missing_required_fields(self, session):
        """Негативный тест: добавление студента без обязательных полей"""
        student = Student(
            first_name="Без",
            last_name="Фамилии"
            # email и group_name отсутствуют
        )
        session.add(student)

        with pytest.raises(Exception):
            session.commit()

        session.rollback()

    # ========== Тесты для изменения (UPDATE) ==========

    def test_update_student_positive(self, session):
        """Позитивный тест: изменение данных студента"""
        # Создаем студента
        student = Student(
            first_name="Старое",
            last_name="Имя",
            email=f"old.name_{id(session)}@example.com",
            group_name="OLD-01"
        )
        session.add(student)
        session.commit()

        # Изменяем данные
        student.first_name = "Новое"
        student.last_name = "Имя"
        student.group_name = "NEW-02"
        session.commit()

        # Проверка
        updated_student = session.query(Student).filter_by(id=student.id).first()
        assert updated_student.first_name == "Новое"
        assert updated_student.last_name == "Имя"
        assert updated_student.group_name == "NEW-02"

    def test_update_student_negative_not_found(self, session):
        """Негативный тест: обновление несуществующего студента"""
        non_existent_student = session.query(Student).filter_by(id=99999).first()
        assert non_existent_student is None

    def test_update_student_negative_invalid_email(self, session):
        """Негативный тест: обновление с некорректным email"""
        student = Student(
            first_name="Валидный",
            last_name="Студент",
            email="valid@example.com",
            group_name="VALID"
        )
        session.add(student)
        session.commit()

        # Пытаемся обновить с уже существующим email
        student2 = Student(
            first_name="Другой",
            last_name="Студент",
            email="valid@example.com",  # Тот же email
            group_name="OTHER"
        )
        session.add(student2)

        with pytest.raises(Exception):
            session.commit()

        session.rollback()

    # ========== Тесты для удаления (DELETE) ==========

    def test_delete_student_positive(self, session):
        """Позитивный тест: физическое удаление студента"""
        # Создаем студента
        student = Student(
            first_name="Удаляемый",
            last_name="Студент",
            email=f"delete.me_{id(session)}@example.com",
            group_name="DELETE"
        )
        session.add(student)
        session.commit()

        student_id = student.id

        # Удаляем
        session.delete(student)
        session.commit()

        # Проверка
        deleted_student = session.query(Student).filter_by(id=student_id).first()
        assert deleted_student is None

    def test_soft_delete_student_positive(self, session):
        """Позитивный тест: мягкое удаление студента (soft delete)"""
        # Создаем студента
        student = Student(
            first_name="Мягко",
            last_name="Удаляемый",
            email=f"soft.delete_{id(session)}@example.com",
            group_name="SOFT",
            is_deleted=False
        )
        session.add(student)
        session.commit()

        # Мягкое удаление
        student.is_deleted = True
        session.commit()

        # Проверка - студент помечен как удаленный
        soft_deleted = session.query(Student).filter_by(id=student.id).first()
        assert soft_deleted.is_deleted is True

        # Проверка - студент не появляется в обычных запросах
        active_students = session.query(Student).filter_by(is_deleted=False).all()
        assert student not in active_students

    def test_delete_student_negative_not_found(self, session):
        """Негативный тест: удаление несуществующего студента"""
        non_existent_student = session.query(Student).filter_by(id=99999).first()
        assert non_existent_student is None

        # Попытка удалить None не вызывает ошибки, но и ничего не удаляет
        if non_existent_student:
            session.delete(non_existent_student)
            session.commit()

    # ========== Дополнительные тесты для других сущностей ==========

    def test_create_course_positive(self, session):
        """Позитивный тест: добавление курса"""
        course = Course(
            title="Python Programming",
            description="Learn Python from scratch",
            credits=5
        )
        session.add(course)
        session.commit()

        assert course.id is not None
        saved_course = session.query(Course).filter_by(id=course.id).first()
        assert saved_course.title == "Python Programming"
        assert saved_course.credits == 5

    def test_update_course_positive(self, session):
        """Позитивный тест: обновление курса"""
        course = Course(
            title="Old Title",
            description="Old description",
            credits=3
        )
        session.add(course)
        session.commit()

        course.title = "New Title"
        course.credits = 4
        session.commit()

        updated = session.query(Course).filter_by(id=course.id).first()
        assert updated.title == "New Title"
        assert updated.credits == 4

    def test_delete_course_with_enrollments(self, session):
        """Тест: удаление курса с предварительной очисткой связей"""
        # Создаем курс
        course = Course(
            title="Course To Delete",
            description="This course will be deleted",
            credits=2
        )
        session.add(course)
        session.commit()

        # Создаем студента
        student = Student(
            first_name="Связанный",
            last_name="Студент",
            email=f"linked.{id(session)}@example.com",
            group_name="LINKED"
        )
        session.add(student)
        session.commit()

        # Создаем запись на курс
        enrollment = Enrollment(
            student_id=student.id,
            course_id=course.id
        )
        session.add(enrollment)
        session.commit()

        # Удаляем запись на курс (сначала связанные данные)
        session.delete(enrollment)
        session.commit()

        # Теперь удаляем курс
        session.delete(course)
        session.commit()

        # Проверка
        deleted_course = session.query(Course).filter_by(id=course.id).first()
        assert deleted_course is None

    def test_create_enrollment_positive(self, session):
        """Позитивный тест: запись студента на курс"""
        # Создаем студента
        student = Student(
            first_name="Записанный",
            last_name="Студент",
            email=f"enrolled.{id(session)}@example.com",
            group_name="ENROLL"
        )
        session.add(student)
        session.commit()

        # Создаем курс
        course = Course(
            title="Enrollment Course",
            description="Course for enrollment test",
            credits=3
        )
        session.add(course)
        session.commit()

        # Создаем запись
        enrollment = Enrollment(
            student_id=student.id,
            course_id=course.id
        )
        session.add(enrollment)
        session.commit()

        assert enrollment.id is not None

        # Проверка
        saved_enrollment = session.query(Enrollment).filter_by(
            student_id=student.id,
            course_id=course.id
        ).first()
        assert saved_enrollment is not None