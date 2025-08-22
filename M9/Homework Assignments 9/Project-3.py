with open('myself.txt', 'w') as file:
    file.write("My name is Tazkeer Dua Samak. I am a girl. I am 15 years old. I study in 12th grade.I live in Lahore, Pakistan.")

with open('my_intro.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print(word)

import os
print("Checking if My_File exists or not...")
if os.path.exists("My_File.txt"): 
    os.remove("My_File.txt")
    print("My_File.txt is removed!")
else:
    print("the file does not exist")

new_file = open('My_File.txt', 'x')
new_file.close()

with open('My_File.txt', 'w') as file:
    file.write("My name is Tazkeer Dua Samak. I am a girl. I am 15 years old. I study in 12th grade.I live in Lahore, Pakistan.")

print("Deleting sample_doc.txt if it exists...")
if os.path.exists("sample_doc.txt"): 
    os.remove("sample_doc.txt")
    print("sample_doc.txt is removed!")
else:
    print("the file does not exist")

