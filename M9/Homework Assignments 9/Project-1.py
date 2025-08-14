file_read = open('std_sub.txt')
print(file_read.read())
file_read.close()

file_write = open('std_sub.txt', "w")
file_write.write("Roy is the class monitor. He is a responsible leader who helps keep the class organized.\n")
file_write.close()

file_append = open('std_sub.txt', "a")
file_append.write("Favorite Subject: Home Economics\n")
file_append.close()