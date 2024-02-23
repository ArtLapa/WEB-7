# additional_queries.py
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Subject, Teacher, Group

engine = create_engine('postgresql://your_username:your_password@localhost:5432/your_database_name')
Session = sessionmaker(bind=engine)
session = Session()

# Додаткові складні запити
def additional_query_1():
    # Середній бал, який певний викладач ставить певному студентові
    pass

def additional_query_2():
    # Оцінки студентів у певній групі з певного предмета на останньому занятті
    pass

session.close()

