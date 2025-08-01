class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_sum(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")
 
expr1 = Expression(5, 10, 15)
expr1.calculate_sum()

expr2 = Expression(1, 2, 3)
expr2.calculate_sum()
