file = open('myself.txt', 'r')
print(file.read())
file.close()

file = open('myself.txt', 'r')
print("\nRead in parts \n")
print(file.read(6))
file.close()

file = open('myself.txt', 'a')
file.write("I am hoping to be a part of either Human Mind Society or Hiking and Mountaineering Society")
file.close()