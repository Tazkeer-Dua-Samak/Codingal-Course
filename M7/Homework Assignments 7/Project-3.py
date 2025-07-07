total_days = int(input("Enter the total number of working days: "))
absent_days = int(input("Enter the total number of days absent: "))
attendance_percentage = ((total_days - absent_days) / total_days) * 100
if attendance_percentage < 75:
    print(f"Your attendance percentage is {attendance_percentage}%. You cannot sit for the exam.")
else:
    print(f"Your attendance percentage is {attendance_percentage}%. You are eligible to sit for the exam.")
