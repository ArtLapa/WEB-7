import sqlite3
from faker import Faker

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

fake = Faker()

cursor.executemany("INSERT INTO groups (group_name) VALUES (?)", [(fake.word(),) for _ in range(10)])

cursor.executemany("INSERT INTO teachers (teacher_name) VALUES (?)", [(fake.name(),) for _ in range(10)])

cursor.executemany("INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)",
                   [(fake.word(), fake.random_int(1, 10)) for _ in range(10)])

cursor.executemany("INSERT INTO students (student_name, group_id) VALUES (?, ?)",
                   [(fake.name(), fake.random_int(1, 10)) for _ in range(10)])

cursor.executemany("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
                   [(fake.random_int(1, 10), fake.random_int(1, 10), fake.random_int(0, 100)) for _ in range(10)])

conn.commit()
conn.close()
