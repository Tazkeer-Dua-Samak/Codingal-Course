def myFunction(n):
    for i in range(0, n+1):
        print("First Loop", i)

    j=1
    while(j<=n+1):
        print("Second Loop", j)
        j=j*2

    for i in range(0,100):
        print("Third Loop", i)

    print("\nTime Complexity: O(n)")


n = int(input("Please enter a number: "))
myFunction(n)
