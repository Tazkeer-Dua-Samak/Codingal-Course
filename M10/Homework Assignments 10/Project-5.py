def binary_to_decimal_manual():
    binary_input = input("Enter a binary number: ") 
    decimal_output = 0
    binary_length = len(binary_input) 

    for i in range(binary_length):
        bit = int(binary_input[binary_length - 1 - i]) 
        decimal_output += bit * (2 ** i) 

    print(f"The decimal equivalent of binary {binary_input} is {decimal_output}")

binary_to_decimal_manual()