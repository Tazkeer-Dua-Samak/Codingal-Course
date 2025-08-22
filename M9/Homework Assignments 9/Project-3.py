with open('my_intro.txt', 'r') as file:
    data = file.readlines()
    print(data)
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print(word)