-- Вывести предметы, по которым есть оценки, и количество оценок
SELECT subject_name, COUNT(*) as grade_count FROM grades
JOIN subjects ON grades.subject_id = subjects.subject_id
GROUP BY subject_name;
