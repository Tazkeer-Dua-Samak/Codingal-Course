def setBit(n):
    if n <= 0:
        print("NOT ALLOWED HERE!!")
    position = 1
    while(n & 1) == 0:
        n >>= 1
        position += 1
    print(position)

number = int(input("Enter a number: "))
setBit(number)