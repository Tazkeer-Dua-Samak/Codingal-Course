def fun1(n):
    return n*(n+1)/2
print(fun1(4))

def fun2(n):
    sum=0
    for i in range(1, n+1):
        sum+=1
    return sum
print(fun2(4))

def fun3(n):
    sum=0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum+=1
    return sum
print(fun3(4))
# Function to convert binary to decimal manually
def binary_to_decimal_manual():
    binary_input = input("Enter a binary number: ")
    decimal_output = 0
    binary_length = len(binary_input)

    for i in range(binary_length):
        bit = int(binary_input[binary_length - 1 - i])  # Get the bit from the end
        decimal_output += bit * (2 ** i)  # Calculate the decimal value

    print(f"The decimal equivalent of binary {binary_input} is {decimal_output}")

# Call the function
binary_to_decimal_manual()
