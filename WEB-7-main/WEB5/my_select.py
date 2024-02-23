# my_select.py
from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Subject, Teacher, Group

engine = create_engine('postgresql://your_username:your_password@localhost:5432/your_database_name')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(Student.student_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.student_id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    return session.query(Student.student_name, func.max(Grade.grade).label('max_grade'))\
        .select_from(Grade).join(Student).join(Subject).filter(Subject.subject_name == subject_name).group_by(Student.student_id).order_by(desc('max_grade')).first()

def select_3(subject_name):
    return session.query(Group.group_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Group).join(Subject).filter(Subject.subject_name == subject_name).group_by(Group.group_id).all()

def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()

def select_5(teacher_name):
    return session.query(Subject.subject_name).join(Teacher).filter(Teacher.teacher_name == teacher_name).all()

def select_6(group_name):
    return session.query(Student.student_name).join(Group).filter(Group.group_name == group_name).all()

def select_7(group_name, subject_name):
    return session.query(Student.student_name, Grade.grade)\
        .join(Group).join(Subject).filter(Group.group_name == group_name, Subject.subject_name == subject_name).all()

def select_8(teacher_name):
    return session.query(Subject.subject_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Teacher).filter(Teacher.teacher_name == teacher_name).group_by(Subject.subject_name).all()

def select_9(student_name):
    return session.query(Subject.subject_name).join(Grade).join(Student).filter(Student.student_name == student_name).all()

def select_10(student_name, teacher_name):
    return session.query(Subject.subject_name).join(Subject.teacher).join(Student).filter(Student.student_name == student_name, Teacher.teacher_name == teacher_name).all()

session.close()
