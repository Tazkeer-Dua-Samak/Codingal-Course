CREATE TABLE IF NOT EXISTS CUSTOMERS2 (
    CUSTOMER_ID TEXT PRIMARY KEY,
    FIRST_NAME TEXT NOT NULL,
    LAST_NAME TEXT NOT NULL,
    DATE_OF_BIRTH DATE,
    PHONE_NUMBER TEXT,
    EMAIL TEXT,
    CITY TEXT,
    MEMBERSHIP_LEVEL TEXT
);

INSERT INTO CUSTOMERS2 (
    CUSTOMER_ID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH,
    PHONE_NUMBER, EMAIL, CITY, MEMBERSHIP_LEVEL
) VALUES
('CUS001', 'Ahmed', 'Rafiq', '1990-04-12', '0302-5512901', 'ahmed.rafiq@example.com', 'Lahore', 'Gold'),
('CUS002', 'Sara', 'Mirza', '1995-09-28', '0315-8823400', 'sara.mirza@example.com', 'Karachi', 'Silver'),
('CUS003', 'Hassan', 'Ali', '1988-02-17', '0333-6604211', 'hassan.ali@example.com', 'Islamabad', 'Platinum'),
('CUS004', 'Maha', 'Zubair', '1993-07-05', '0301-7712305', 'maha.zubair@example.com', 'Rawalpindi', 'Regular'),
('CUS005', 'Umar', 'Shahid', '1985-11-23', '0321-9982104', 'umar.shahid@example.com', 'Faisalabad', 'Gold'),
('CUS006', 'Areeba', 'Khalid', '1997-06-19', '0345-6619034', 'areeba.khalid@example.com', 'Lahore', 'Silver'),
('CUS007', 'Rizwan', 'Iqbal', '1989-01-08', '0308-5531298', 'rizwan.iqbal@example.com', 'Karachi', 'Regular'),
('CUS008', 'Nida', 'Farooq', '1994-03-15', '0331-4419088', 'nida.farooq@example.com', 'Multan', 'Platinum'),
('CUS009', 'Talha', 'Arshad', '1992-12-06', '0317-7723044', 'talha.arshad@example.com', 'Lahore', 'Gold'),
('CUS010', 'Emaan', 'Saleem', '1996-05-21', '0340-5518922', 'emaan.saleem@example.com', 'Hyderabad', 'Regular'),
('CUS011', 'Yousuf', 'Hussain', '1987-08-30', '0334-9098123', 'yousuf.hussain@example.com', 'Quetta', 'Silver'),
('CUS012', 'Laiba', 'Javed', '1998-10-11', '0307-8819022', 'laiba.javed@example.com', 'Lahore', 'Gold'),
('CUS013', 'Shayan', 'Malik', '1991-03-04', '0320-5512387', 'shayan.malik@example.com', 'Sialkot', 'Platinum'),
('CUS014', 'Fatima', 'Yasir', '1993-01-26', '0311-6623099', 'fatima.yasir@example.com', 'Islamabad', 'Silver'),
('CUS015', 'Zain', 'Khurshid', '1986-09-24', '0309-7741092', 'zain.khurshid@example.com', 'Karachi', 'Gold'),
('CUS016', 'Amna', 'Rashid', '1995-12-18', '0342-9081120', 'amna.rashid@example.com', 'Peshawar', 'Regular'),
('CUS017', 'Fahad', 'Saeed', '1990-06-02', '0316-5532100', 'fahad.saeed@example.com', 'Lahore', 'Platinum'),
('CUS018', 'Hiba', 'Rehman', '1997-04-14', '0335-6721108', 'hiba.rehman@example.com', 'Karachi', 'Silver'),
('CUS019', 'Adnan', 'Yousaf', '1989-02-27', '0306-9987712', 'adnan.yousaf@example.com', 'Rawalpindi', 'Gold'),
('CUS020', 'Nimra', 'Khan', '1998-07-09', '0344-7712204', 'nimra.khan@example.com', 'Lahore', 'Regular');

SELECT * FROM CUSTOMERS2;

SELECT * FROM CUSTOMERS2
WHERE FIRST_NAME LIKE 'A%';

SELECT FIRST_NAME, LAST_NAME, CITY
FROM CUSTOMERS2
WHERE LOWER(FIRST_NAME) LIKE '%or%'
   OR LOWER(LAST_NAME) LIKE '%or%';
