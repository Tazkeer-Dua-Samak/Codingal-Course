my_set = {1, 2, 2, 3, 4, 4, 4}
print("Set: ", my_set)

my_set.add(5)
print("Updated Set: ", my_set)

set_1 = my_set
set_2 = {2, 4, 4, 6}

print("\nSet 1: ", set_1)
print("Set 2: ", set_2)
print("Difference: ")
print(set_1.difference(set_2))
print("Symmetric Difference :")
print(set_1.symmetric_difference(set_2))#Union-Intersection