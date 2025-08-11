file1 = open('myself.txt', 'r')
file2 = open('myselfupdated.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('I')):
        print(line)
        file2.write(line)

file2.close()
file1.close()