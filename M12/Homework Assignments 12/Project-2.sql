CREATE TABLE IF NOT EXISTS CUSTOMERS (
    CUSTOMER_ID INTEGER PRIMARY KEY,
    NAME TEXT,
    GENDER TEXT,
    CITY TEXT,
    GRADE INTEGER
);


INSERT INTO CUSTOMERS (CUSTOMER_ID, NAME, GENDER, CITY, GRADE)
VALUES
    (991, 'Alice Johnson', 'Female', 'New York', 180),
    (992, 'Michael Smith', 'Male', 'Los Angeles', 95),
    (993, 'Sophia Brown', 'Female', 'Chicago', 150),
    (994, 'James Williams', 'Male', 'New York', 120),
    (995, 'Emily Davis', 'Female', 'Houston', 85),
    (996, 'Daniel Miller', 'Male', 'Miami', 102),
    (997, 'Olivia Wilson', 'Female', 'Boston', 75),
    (998, 'Ethan Moore', 'Male', 'Seattle', 200),
    (999, 'Ava Taylor', 'Female', 'San Francisco', 92),
    (1000, 'Benjamin Anderson', 'Male', 'New York', 140),
    (1001, 'Charlotte Thomas', 'Female', 'Dallas', 88),
    (1002, 'Lucas Jackson', 'Male', 'Denver', 130),
    (1003, 'Amelia White', 'Female', 'Atlanta', 170),
    (1004, 'Henry Harris', 'Male', 'New York', 78),
    (1005, 'Mia Martin', 'Female', 'Philadelphia', 96),
    (1006, 'William Thompson', 'Male', 'Phoenix', 110),
    (1007, 'Isabella Garcia', 'Female', 'San Diego', 190),
    (1008, 'Jacob Martinez', 'Male', 'New York', 145),
    (1009, 'Harper Robinson', 'Female', 'Las Vegas', 82),
    (2000, 'Elijah Clark', 'Male', 'Orlando', 175);

SELECT * FROM CUSTOMERS;
SELECT * FROM CUSTOMERS WHERE CITY = 'New York' OR GRADE > 100;

SELECT * FROM CUSTOMERS;
SELECT * FROM CUSTOMERS WHERE CITY = 'New York' AND GRADE > 100;