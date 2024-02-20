# additional_queries.py
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Subject, Teacher, Group

engine = create_engine('postgresql://username:password@localhost:5432/your_database_name')

Session = sessionmaker(bind=engine)
session = Session()

# Ваші додаткові запити

session.close()
