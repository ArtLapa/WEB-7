# seed.py
from faker import Faker
from sqlalchemy import create_engine
from models import Base, Student, Group, Teacher, Subject, Grade

fake = Faker()

# З'єднання із базою даних
engine = create_engine('postgresql://your_username:your_password@localhost:5432/your_database_name')
Base.metadata.create_all(engine)

# Наповнення таблиць даними
with engine.connect() as connection:
    for _ in range(30):
        group = Group(group_name=fake.word())
        connection.execute(Group.__table__.insert().values(group_name=group.group_name))

    for _ in range(3):
        teacher = Teacher(teacher_name=fake.name())
        connection.execute(Teacher.__table__.insert().values(teacher_name=teacher.teacher_name))

    for _ in range(5):
        subject = Subject(subject_name=fake.word(), teacher_id=fake.random_int(min=1, max=3))
        connection.execute(Subject.__table__.insert().values(subject_name=subject.subject_name, teacher_id=subject.teacher_id))

    for _ in range(50):
        student = Student(student_name=fake.name(), group_id=fake.random_int(min=1, max=10))
        connection.execute(Student.__table__.insert().values(student_name=student.student_name, group_id=student.group_id))

    for _ in range(100):
        grade = Grade(student_id=fake.random_int(min=1, max=50), subject_id=fake.random_int(min=1, max=5), grade=fake.random_int(min=50, max=100))
        connection.execute(Grade.__table__.insert().values(student_id=grade.student_id, subject_id=grade.subject_id, grade=grade.grade))
