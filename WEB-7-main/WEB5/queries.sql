-- queries.sql
-- query_1.sql
SELECT student_id, AVG(grade) as avg_grade
FROM grades
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 5;

-- query_2.sql
SELECT student_id, AVG(grade) as avg_grade
FROM grades
WHERE subject_id = 1  -- Замініть на конкретний ідентифікатор предмета
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 1;

-- query_3.sql
SELECT groups.group_name, AVG(grades.grade) as avg_grade
FROM grades
JOIN students ON grades.student_id = students.student_id
JOIN groups ON students.group_id = groups.group_id
WHERE grades.subject_id = 1  -- Замініть на конкретний ідентифікатор предмета
GROUP BY groups.group_id;

-- query_4.sql
SELECT AVG(grade) as avg_grade
FROM grades;

-- query_5.sql
SELECT subjects.subject_name
FROM subjects
WHERE subjects.teacher_id = 1  -- Замініть на конкретний ідентифікатор викладача;

-- query_6.sql
SELECT students.student_name
FROM students
WHERE students.group_id = 1  -- Замініть на конкретний ідентифікатор групи;

-- query_7.sql
SELECT students.student_name, grades.grade
FROM students
JOIN grades ON students.student_id = grades.student_id
WHERE students.group_id = 1 AND grades.subject_id = 1;  -- Замініть на конкретні ідентифікатори групи та предмета;

-- query_8.sql
SELECT teachers.teacher_name, AVG(grades.grade) as avg_grade
FROM teachers
JOIN subjects ON teachers.teacher_id = subjects.teacher_id
JOIN grades ON subjects.subject_id = grades.subject_id
GROUP BY teachers.teacher_id;

-- query_9.sql
SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
WHERE grades.student_id = 1;  -- Замініть на конкретний ідентифікатор студента;

-- query_10.sql
SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
WHERE grades.student_id = 1 AND subjects.teacher_id = 1;  -- Замініть на конкретні ідентифікатори студента та викладача;
