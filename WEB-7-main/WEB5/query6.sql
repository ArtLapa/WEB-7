-- Вывести студентов, имена их групп, предметы и оценки
SELECT student_name, group_name, subject_name, grade FROM students
JOIN groups ON students.group_id = groups.group_id
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id;
