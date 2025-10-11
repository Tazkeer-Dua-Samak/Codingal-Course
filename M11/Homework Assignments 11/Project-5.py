def longest_consecutive_ones(n):
    binary = bin(n)[2:]  # convert to binary string without '0b' (that I learned is used in this conversion) so that the program can correctly count the number of consecutive 1's
    count_one = 0
    max_count = 0

    for bit in binary:
        if bit == '1':
            count_one += 1
            if count_one > max_count:
                max_count = count_one
        else:
            count_one = 0

    return max_count

user_input = int(input("Enter a number: "))
result = longest_consecutive_ones(user_input)
print("Longest consecutive 1's length:", result)
