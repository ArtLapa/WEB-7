-- Вывести имена студентов и их оценки
SELECT student_name, grade FROM students
JOIN grades ON students.student_id = grades.student_id;
