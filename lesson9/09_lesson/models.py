"""Модели базы данных SQLAlchemy"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Student(Base):
    """Модель студента"""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    group_name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    is_deleted = Column(Boolean, default=False)  # Для soft delete

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name})>"


class Course(Base):
    """Модель курса"""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    credits = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title})>"


class Enrollment(Base):
    """Модель записи на курс (связь многие-ко-многим)"""
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, nullable=False)
    course_id = Column(Integer, nullable=False)
    enrolled_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"
