def myFunction1(n):
    if n <= 0:
        return
    for i in range(0, n+1):
        print("Codingal")
    myFunction1(n//2)
    myFunction1(n//3)

def myFunction2(n):
    if n <= 1:
        print("Codingal")
    myFunction2(n-1)

print("Recurrence relation of myFunction1: ")
print("T(n) = T(n/2) + T(n/3) + O(n)")
print("\nRecurrence relation of myFunction1: ")
print("T(n) = T(n-1) + O(1)")