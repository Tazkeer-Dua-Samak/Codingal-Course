import matplotlib.pyplot as plt

students_names = ["Aisha", "Ali", "Bilal", "Ramesh", "Maria", "Sarah", "Waseem"]
students_marks = [43, 12, 34, 32, 50, 25, 15]

marks_perc = [(marks / 50) * 100 for marks in students_marks]

def marks_line_chart():
    plt.plot(students_names, students_marks, marker='o', linestyle='-', color='blue')
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks (out oof 50)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def percentage_bar_chart():
    plt.bar(students_names, marks_perc, color='green')
    plt.title("Students Percentage Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

marks_line_chart()
percentage_bar_chart()