file_read = open('myself.txt', 'r')
print("File in Read Mode - ")
print(file_read.read())
file_read.close()

file_write = open('myself.txt', 'w')
file_write.write("File in write mode...")
file_write.write("Hi! I am Penguin. I am a year old.")
file_write.close()

file_append = open('myself.txt', 'a')
file_append.write("\n File in write mode...")
file_append.write("Hi! I am Penguin. I am a year old.")
file_append.close()