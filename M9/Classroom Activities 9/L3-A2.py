new_file = open('my_file.txt', 'x')
new_file.close()

import os
print("Checking if my_file exists or not...")
if os.path.exists("my_file.txt"): 
    os.remove("my_file.txt")
    print("my_file.txt is removed!")
else:
    print("the file does not exist")

my_file = open("my_file.txt", 'w')
my_file.write("Hi! I am a penguin as well!. I am 2 years old.")
my_file.close()

os.remove('my_file.txt')

#To delete a folder use:
#os.rmdir('Folder_name')