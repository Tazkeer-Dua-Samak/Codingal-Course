class student:
    grade = 11
    name = "Tazkeer Dua Samak"

    def introduction(self):
        print("Hi! I am a student!")

    def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()