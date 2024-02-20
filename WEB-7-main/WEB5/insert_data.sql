-- insert_data.sql
-- Insert data for students
INSERT INTO students (student_name, group_id) VALUES
    (Faker()::name, 1),
    (Faker()::name, 2);
    -- Add more students...

-- Insert data for groups
INSERT INTO groups (group_name) VALUES
    (Faker()::word),
    (Faker()::word);
    -- Add more groups...

-- Insert data for teachers
INSERT INTO teachers (teacher_name) VALUES
    (Faker()::name),
    (Faker()::name);
    -- Add more teachers...

-- Insert data for subjects
INSERT INTO subjects (subject_name, teacher_id) VALUES
    (Faker()::word, 1),
    (Faker()::word, 2);
    -- Add more subjects...

-- Insert data for grades
INSERT INTO grades (student_id, subject_id, grade) VALUES
    (1, 1, Faker()::number_between(50, 100)),
    (2, 1, Faker()::number_between(50, 100));

-- Вставка даних для студентів
INSERT INTO students (student_name, group_id) VALUES
    ('Student1', 1),
    ('Student2', 2),
    -- Додайте ще студентів...

-- Вставка даних для груп
INSERT INTO groups (group_name) VALUES
    ('GroupA'),
    ('GroupB'),
    -- Додайте ще груп...

-- Вставка даних для викладачів
INSERT INTO teachers (teacher_name) VALUES
    ('Teacher1'),
    ('Teacher2'),
    -- Додайте ще викладачів...

-- Вставка даних для предметів
INSERT INTO subjects (subject_name, teacher_id) VALUES
    ('Subject1', 1),
    ('Subject2', 2),
    -- Додайте ще предмети...

-- Вставка даних для оцінок
INSERT INTO grades (student_id, subject_id, grade) VALUES
    (1, 1, 90),
    (2, 1, 85),
    -- Додайте ще оцінки...
