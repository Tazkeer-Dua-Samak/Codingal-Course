import math

class Shape:
    def __init__(self, name):
        self.name = name  

    def display_name(self):
        print(f"This is a {self.name}.")

class Polygon(Shape):
    def __init__(self, sides, length):
        super().__init__("Polygon")
        self.sides = sides
        self.length = length

    def calculate_area(self):
        area = (self.sides * (self.length ** 2)) / (4 * math.tan(math.pi / self.sides))
        return area

def main():
    sides = int(input("Enter the number of sides of the polygon: "))
    length = float(input("Enter the length of each side: "))
    
    polygon = Polygon(sides, length)
    
    polygon.display_name() 
    area = polygon.calculate_area()
    print(f"The area of the polygon is: {area:.2f}")

obj = main()