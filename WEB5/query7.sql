-- Вывести количество студентов в каждой группе
SELECT group_name, COUNT(*) as student_count FROM students
JOIN groups ON students.group_id = groups.group_id
GROUP BY group_name;
