num = int(input("Enter a number to check : "))

if num>50:
    print("Number is greater than 50")
    if num%2==0:
        print("and it is even too")
    else:
        print("and it is odd too")
else:
    print("Number is less than 50")
    if num%2==0:
        print("and it is even too")
    else:
        print("and it is odd too")