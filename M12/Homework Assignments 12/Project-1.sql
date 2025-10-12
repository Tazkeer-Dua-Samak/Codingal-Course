CREATE TABLE IF NOT EXISTS Students (
    Student_id INTEGER PRIMARY KEY,
    Student_name TEXT,
    Student_gender TEXT,
    Student_subject TEXT,
    Student_mobile INTEGER
);

INSERT INTO Students (Student_id, Student_name, Student_gender, Student_mobile, Student_subject) VALUES
    (5001, 'Hannah Wheeler', 'Female', 206-342-8631, 'Biology'),
    (5002, 'Kenneth Gray', 'Male', 717-550-1675, 'Computer Science'),
    (5005, 'Sarah Burton', 'Female', 248-762-0356, 'Computer Science'),
    (5006, 'Zander Donaldson', 'Male', 253-644-2182, 'Biology'),
    (5007, 'Natasha Collier', 'Female', 212-658-3916, 'Computer Science'),
    (5003, 'Edison Dean', 'Male', 209-300-2557, 'Biology');

SELECT * FROM Students

SELECT * FROM Students
WHERE Student_subject == "Computer Science"