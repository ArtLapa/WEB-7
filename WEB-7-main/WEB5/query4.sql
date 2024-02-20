-- Вывести студентов и их группы
SELECT student_name, group_name FROM students
JOIN groups ON students.group_id = groups.group_id;
