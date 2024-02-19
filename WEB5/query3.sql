-- Вывести имена предметов и соответствующих им преподавателей
SELECT subject_name, teacher_name FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.teacher_id;
