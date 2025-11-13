CREATE TABLE IF NOT EXISTS EMPLOYEES (
    EMPLOYEE_ID INTEGER PRIMARY KEY,
    EMPLOYEE_NAME TEXT,
    EMPLOYEE_GENDER TEXT,
    EMPLOYEE_DESIGNATION TEXT,
    EMPLOYEE_QUALIFICATION TEXT,
    EMPLOYEE_SALARY INTEGER
);

INSERT INTO EMPLOYEES (EMPLOYEE_ID, EMPLOYEE_NAME, 
    EMPLOYEE_GENDER, EMPLOYEE_DESIGNATION, 
    EMPLOYEE_QUALIFICATION, EMPLOYEE_SALARY) VALUES

    (1, 'Alice Johnson', 'Female', 'Manager', 'MBA', 85000),
    (2, 'Michael Smith', 'Male', 'Software Engineer', 'BSc Computer Science', 72000),
    (3, 'Sophia Brown', 'Female', 'HR Officer', 'BA Psychology', 56000),
    (4, 'James Williams', 'Male', 'Accountant', 'BCom', 60000),
    (5, 'Emily Davis', 'Female', 'Data Analyst', 'BSc Statistics', 67000),
    (6, 'Daniel Miller', 'Male', 'Project Lead', 'MBA', 91000),
    (7, 'Olivia Wilson', 'Female', 'UI/UX Designer', 'BFA Design', 65000),
    (8, 'Ethan Moore', 'Male', 'Technician', 'Diploma Electronics', 52000),
    (9, 'Ava Taylor', 'Female', 'Marketing Executive', 'BBA', 59000),
    (10, 'Benjamin Anderson', 'Male', 'Software Developer', 'MSc Computer Science', 78000),
    (11, 'Charlotte Thomas', 'Female', 'Receptionist', 'High School', 40000),
    (12, 'Lucas Jackson', 'Male', 'Network Administrator', 'BSc IT', 71000),
    (13, 'Amelia White', 'Female', 'Business Analyst', 'MBA', 88000),
    (14, 'Henry Harris', 'Male', 'Sales Manager', 'BBA', 73000),
    (15, 'Mia Martin', 'Female', 'Content Writer', 'BA English', 54000);

SELECT * FROM EMPLOYEES;
SELECT SUM(EMPLOYEE_SALARY) AS TOTAL_SALARY
FROM EMPLOYEES;

SELECT * FROM EMPLOYEES;
SELECT COUNT(EMPLOYEE_ID) AS TOTAL_EMPLOYEES
FROM EMPLOYEES;

SELECT * FROM EMPLOYEES;
SELECT MAX(EMPLOYEE_SALARY) AS HIGHEST_SALARY
FROM EMPLOYEES;

SELECT * FROM EMPLOYEES;
SELECT MIN(EMPLOYEE_SALARY) AS LOWEST_SALARY
FROM EMPLOYEES;

SELECT * FROM EMPLOYEES;
SELECT COUNT(DISTINCT EMPLOYEE_DESIGNATION) AS TOTAL_DEPARTMENTS
FROM EMPLOYEES;

SELECT * FROM EMPLOYEES;
SELECT AVG(EMPLOYEE_SALARY) AS AVERAGE_SALARY
FROM EMPLOYEES;