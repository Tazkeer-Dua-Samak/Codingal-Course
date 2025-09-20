def setOrNot(number, n):
    if number & (1 << (n - 1)):
        print("SET")
    else:
        print("NOT SET")
        
number = int(input("Enter a number: "))
n = int(input("Enter the bit position: "))
setOrNot(number, n)