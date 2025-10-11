def printSubStrings(s, size):
    powerSetSize = 1 << size  # same as 2^size but using bitwise

    for outer in range(1, powerSetSize):  # start from 1 to skip empty substring
        result = ""
        for inner in range(size):
            if (outer & (1 << inner)) > 0:
                result += s[inner]
        print(result)


string = input("Enter a string: ")
printSubStrings(string, len(string))