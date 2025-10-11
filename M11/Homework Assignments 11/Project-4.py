def is_power_of_8(n):
    if n <= 0:
        return False

    if (n & (n - 1)) != 0:
        return False

    shifts = 0
    
    while n > 1:
        n >>= 1
        shifts += 1

    return shifts % 3 == 0


user_input = int(input("Enter a number: "))
if is_power_of_8(user_input):
    print("It is a power of 8")
else:
    print("It is NOT a power of 8")
