def reverse_bits(n):
    reversed_num = 0
    bits = n.bit_length()

    for _ in range(bits):
        reversed_num <<= 1
        reversed_num |= (n & 1)
        n >>= 1

    return reversed_num

user_input = int(input("Enter a number: "))
result = reverse_bits(user_input)
print("Reversed bits:", result)
