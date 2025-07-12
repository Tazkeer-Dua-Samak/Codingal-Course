def fibonacci_sequence(length):
    a = 0
    b = 1
    for i in range(length):
        print(a, end=' ')
        a, b = b, a + b
length = int(input("Enter the length of the Fibonacci sequence: "))
fibonacci_sequence(length)