my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, "HI!", 98.65)
print(my_tuple)

my_tuple = ("cat", [54, 675, 235], (58685, 986, 436))
print(my_tuple)

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])

n_tuple = ("cat", [54, 675, 235], (58685, 986, 436))
print(n_tuple[0][2])
print(n_tuple[1][1])

print("Sliced", my_tuple[1:4])

for letter in (my_tuple):
    print("Hello", letter)