# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    # ... (зазначте код для моделі Student)

class Group(Base):
    # ... (зазначте код для моделі Group)

class Teacher(Base):
    # ... (зазначте код для моделі Teacher)

class Subject(Base):
    # ... (зазначте код для моделі Subject)

class Grade(Base):
    # ... (зазначте код для моделі Grade)
