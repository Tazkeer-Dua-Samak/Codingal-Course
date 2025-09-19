def myFunction(n):
    for i in range(0, n+1):
        print("First Loop: ", i)
    print("Time Complexity of First Loop: O(n)")

    j = 1    
    while (j <= n+1):
        print("Second Loop: ", j)
    print("Time Complexity of Second Loop: O(log n)")

    for i in range(0, 10):
        print("Third Loop: ", i)
    print("Time Complexity of Third Loop: O(1)")

    print("\nOverall Time Complexity is: O(n)")

n = int(input("Enter a number: "))
myFunction(n)