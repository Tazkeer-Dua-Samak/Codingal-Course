with open('std_sub.txt', 'r') as file:
    print("Printing Full contents\n")
    print(file.read())

with open('std_sub.txt', 'r') as file:
    print("\nPrinting the first ten characters:\n")
    print(file.read(10))

with open('std_sub.txt', 'r') as file:
    print("\nPrinting the first line:\n")
    print(file.readline())

with open('std_sub.txt', 'r') as file:
    print("\nPrinting the first four non-empty lines:\n")
    count = 0
    for line in file:
        if line.strip():
            print(line, end='')  
            count += 1
        if count == 4:
            break #i learnt that this thing breaks the loop early if my condition is met!

with open('std_sub.txt', 'r') as file:
    print("\n\nPrinting all lines one by one:\n")
    for line in file:
        print(line, end='') 

#I researched some stuff about file handling in python and turns out, if i use "with open(...)" then it automatically closes the opened file
#also learned that ".strip()" can be used to skip empty lines!
#and lastly, using end='' can remove extra newlines (\n) so it does not look weird because "line" already has a newline,