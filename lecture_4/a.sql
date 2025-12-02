-- Create tables: students and grades
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER
);

CREATE TABLE  grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER CHECK(grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Insert sample data
INSERT INTO students(full_name, birth_year)
VALUES
   ('Alice Johnson', 2005),
   ('Brian Smith', 2004),
   ('Carla Reyes', 2006),
   ('Daniel Kim', 2005),
   ('Eva Thompson', 2003),
   ('Felix Nguyen', 2007),
   ('Grace Patel', 2005),
   ('Henry Lopez', 2004),
   ('Isabella Martinez', 2006);

INSERT INTO grades(student_id, subject, grade)
VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 72),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

-- Index by student_id to speed up JOIN and search
CREATE INDEX idx_grades_student_id ON grades(student_id);

-- Index by name to search for students
CREATE INDEX idx_students_full_name ON students(full_name);

-- Find all grades for a specific student (Alice Johnson)
SELECT
    students.full_name,
    grades.subject,
    grades.grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE students.full_name = 'Alice Johnson';

-- Calculate the average grade per student
SELECT
    students.full_name,
    ROUND(AVG(grades.grade), 2) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY avg_grade DESC;

-- List all students born after 2004
SELECT
    id,
    full_name,
    birth_year
FROM students
WHERE birth_year > 2004;

-- Create a query that lists all subjects and their average grades
SELECT
    subject,
    ROUND(AVG(grade), 2) AS avg_grade
FROM grades
GROUP BY subject
ORDER BY avg_grade DESC;

-- Find the top 3 students with the highest average grades
SELECT
    students.full_name,
    ROUND(AVG(grades.grade), 2) AS average
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY average DESC
LIMIT 3;

-- Show all students who have scored below 80 in any subject
SELECT DISTINCT
    students.full_name,
    grades.grade,
    grades.subject
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.grade < 80
ORDER BY grades.grade ASC;