import math

def calculate_polygon_area(sides, length):
    area = (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))
    return area

def main():
    sides = int(input("Enter the number of sides of the polygon: "))
    length = float(input("Enter the length of each side: "))
    area = calculate_polygon_area(sides, length)
    print(f"The area of the polygon is: {area:.2f}")

if __name__ == "__main__":
    main()