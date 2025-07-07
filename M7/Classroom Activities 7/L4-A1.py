num = int(input("Enter a number whose table you want to print : "))
print(f"Table of {num}")
for i in range(1, 11):
    mul = num*i
    print("%d x %d = %d" % (num, i, mul))