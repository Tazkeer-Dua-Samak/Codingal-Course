def factorial(n):
    if n<0:
        return("Invalid Entry")
    elif n==1 or n==0:
        return(1)
#recursion
    return(n*factorial(n-1))
n = int(input("Enter the number whose factorial you want to find : "))
factorial_ = factorial(n)
try:
    print("%d! = %d" %(n, factorial_))
except:
    print(factorial_)