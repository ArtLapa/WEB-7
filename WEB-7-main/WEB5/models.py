# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.group_id'))
    grades = relationship('Grade', back_populates='student')

class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(50), nullable=False)
    students = relationship('Student', back_populates='group')

class Teacher(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(255), nullable=False)
    subjects = relationship('Subject', back_populates='teacher')

class Subject(Base):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(255), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    grades = relationship('Grade', back_populates='subject')
    teacher = relationship('Teacher', back_populates='subjects')

class Grade(Base):
    __tablename__ = 'grades'
    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    grade = Column(Integer, nullable=False)
    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')

