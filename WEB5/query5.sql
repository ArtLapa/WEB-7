-- Вывести предметы, имена преподавателей и оценки студентов
SELECT subject_name, teacher_name, grade FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
JOIN grades ON subjects.subject_id = grades.subject_id;
