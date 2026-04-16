"""Автотесты для модели Student"""

from datetime import datetime
from models import Student


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

    def test_unique_email_constraint(self, db_session, sample_student):
        """Тест уникальности email (негативный)"""
        db_session.add(sample_student)
        db_session.commit()

        second_student = Student(
            first_name="Сергей",
            last_name="Сидоров",
            email="ivan@test.com",
            course=2,
            is_active=True
        )
        db_session.add(second_student)

        with pytest.raises(Exception):
            db_session.commit()
        db_session.rollback()