-- Вывести топ-3 студентов с наивысшими оценками
SELECT student_name, grade FROM grades
JOIN students ON grades.student_id = students.student_id
ORDER BY grade DESC
LIMIT 3;
