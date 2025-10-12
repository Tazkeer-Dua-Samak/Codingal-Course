def printSubStrings(s):
    size = len(s)
    
    for i in range(1, 1 << size):
        substring = ""  
        for j in range(size):
            if (i & (1 << j)) > 0:
                substring += s[j]
        print(substring)

string = input("Enter a string: ")
printSubStrings(string)
