myFunction1_calls = 0
myFunction2_calls = 0

def myFunction1(n):
    global myFunction1_calls #this global means that the variable "myFunction1_calls" can be modified in this function
    if n <= 0:
        return
    myFunction1_calls += 1
    for i in range(0, n + 1):
        pass 
    myFunction1(n // 2)
    myFunction1(n // 3)

def myFunction2(n):
    global myFunction2_calls
    if n <= 1:
        myFunction2_calls += 1
        return
    myFunction2_calls += 1
    myFunction2(n - 1)

n = 100

myFunction1_calls = 0
myFunction1(n)
print(f"Number of calls to myFunction1 for n={n}: {myFunction1_calls}")

myFunction2_calls = 0
myFunction2(n)
print(f"Number of calls to myFunction2 for n={n}: {myFunction2_calls}")