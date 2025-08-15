with open('myself.txt', 'w') as file:
    file.write("Hi! I am back!!!!")

with open('myself.txt', 'r') as file:
    data = file.readlines()
    print(data)
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print(word)