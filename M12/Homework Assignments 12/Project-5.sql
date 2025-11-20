CREATE TABLE IF NOT EXISTS EMPLOYEE2 (
    EMPLOYEE_ID TEXT PRIMARY KEY,
    FIRST_NAME TEXT NOT NULL,
    LAST_NAME TEXT NOT NULL,
    DATE_OF_BIRTH DATE,       
    PHONE_NUMBER TEXT,
    DEPARTMENT TEXT,
    SALARY INTEGER, 
    DESIGNATION TEXT
);

INSERT INTO EMPLOYEE2 (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, PHONE_NUMBER, DEPARTMENT, SALARY, DESIGNATION) VALUES 
    ('EMP001', 'Ayesha', 'Khan', '1990-03-15', '0301-5551234', 'Human Resources', 85000, 'HR Officer'),
    ('EMP002', 'Bilal', 'Sheikh', '1988-07-22', '0320-4478910', 'Finance', 120000, 'Senior Accountant'),
    ('EMP003', 'Zara', 'Malik', '1995-01-10', '0312-6690044', 'IT', 150000, 'Software Engineer'),
    ('EMP004', 'Hassan', 'Raza', '1992-12-02', '0333-9031122', 'IT', 190000, 'System Administrator'),
    ('EMP005', 'Fatima', 'Siddiqui', '1989-05-28', '0306-1189233', 'Marketing', 110000, 'Marketing Executive'),
    ('EMP006', 'Usman', 'Farooq', '1993-11-14', '0345-7712009', 'Operations', 98000, 'Operations Analyst'),
    ('EMP007', 'Laiba', 'Naeem', '1996-04-05', '0309-5512877', 'Customer Support', 70000, 'Support Representative'),
    ('EMP008', 'Omar', 'Hashmi', '1985-09-19', '0335-6642091', 'Finance', 160000, 'Finance Manager'),
    ('EMP009', 'Sana', 'Iqbal', '1994-02-23', '0311-4438206', 'Human Resources', 90000, 'Recruitment Specialist'),
    ('EMP010', 'Talha', 'Mirza', '1991-08-08', '0302-5523100', 'Logistics', 105000, 'Logistics Coordinator'),
    ('EMP011', 'Hiba', 'Rizwan', '1997-06-17', '0344-9076123', 'IT', 140000, 'UI/UX Designer'),
    ('EMP012', 'Arsalan', 'Shah', '1987-10-03', '0331-7629845', 'Marketing', 135000, 'Brand Manager'),
    ('EMP013', 'Nimra', 'Javed', '1998-03-30', '0307-8891022', 'Customer Support', 68000, 'Call Center Agent'),
    ('EMP014', 'Adnan', 'Khattak', '1986-01-25', '0316-5519920', 'Operations', 125000, 'Operations Supervisor'),
    ('EMP015', 'Maryam', 'Zafar', '1992-07-11', '0321-7725410', 'Administration', 95000, 'Admin Officer'),
    ('EMP016', 'Kashif', 'Mehmood', '1984-04-29', '0340-1187420', 'Procurement', 150000, 'Procurement Manager'),
    ('EMP017', 'Eman', 'Shoukat', '1995-09-04', '0334-6732109', 'Finance', 100000, 'Junior Accountant'),
    ('EMP018', 'Shahzaib', 'Anwar', '1990-11-07', '0308-5529988', 'Sales', 130000, 'Sales Executive'),
    ('EMP019', 'Muneeb', 'Qureshi', '1989-02-16', '0343-9017762', 'IT', 200000, 'Senior Software Engineer'),
    ('EMP020', 'Ayra', 'Hassan', '1996-12-21', '0315-7712004', 'Research', 145000, 'Research Analyst');

SELECT * FROM EMPLOYEE2;

SELECT * FROM EMPLOYEE2
WHERE SALARY BETWEEN 90000 AND 150000;

SELECT * FROM EMPLOYEE2
WHERE DATE_OF_BIRTH BETWEEN '1990-01-01' AND '1995-12-31';

SELECT * FROM EMPLOYEE2
WHERE SALARY = 120000;