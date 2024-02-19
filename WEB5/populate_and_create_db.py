import sqlite3
from faker import Faker

def create_and_populate_database():
    # Создаем соединение с базой данных
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Создаем объект Faker для генерации фальшивых данных
    fake = Faker()

    # Создаем таблицы
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            group_id INTEGER PRIMARY KEY,
            group_name TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY,
            teacher_name TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            subject_id INTEGER PRIMARY KEY,
            subject_name TEXT NOT NULL,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            group_id INTEGER,
            FOREIGN KEY (group_id) REFERENCES groups(group_id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER CHECK (grade BETWEEN 0 AND 100),
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        );
    ''')

    # Вставляем данные для групп
    cursor.executemany("INSERT INTO groups (group_name) VALUES (?)", [(fake.word(),) for _ in range(10)])

    # Вставляем данные для преподавателей
    cursor.executemany("INSERT INTO teachers (teacher_name) VALUES (?)", [(fake.name(),) for _ in range(10)])

    # Вставляем данные для предметов
    cursor.executemany("INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)",
                       [(fake.word(), fake.random_int(1, 10)) for _ in range(10)])

    # Вставляем данные для студентов
    cursor.executemany("INSERT INTO students (student_name, group_id) VALUES (?, ?)",
                       [(fake.name(), fake.random_int(1, 10)) for _ in range(10)])

    # Вставляем данные для оценок
    cursor.executemany("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
                       [(fake.random_int(1, 10), fake.random_int(1, 10), fake.random_int(0, 100)) for _ in range(10)])

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_populate_database()
