-- Вывести средние оценки по предметам
SELECT subject_name, AVG(grade) as average_grade FROM grades
JOIN subjects ON grades.subject_id = subjects.subject_id
GROUP BY subject_name;

