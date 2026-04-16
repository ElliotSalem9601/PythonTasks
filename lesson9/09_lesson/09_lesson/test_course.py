"""Автотесты для модели Course"""

from models import Course


class TestCourseCRUD:
    """Тесты CRUD операций для курса"""

    def test_create_course(self, db_session, sample_course):
        """Тест добавления курса"""
        db_session.add(sample_course)
        db_session.commit()

        assert sample_course.id is not None
        assert sample_course.title == "Python для начинающих"
        assert sample_course.credits == 5

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