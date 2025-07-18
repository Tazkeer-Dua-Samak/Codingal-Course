lst = ['Bittergourd', 'Aubergine', 'Capsicum', 'Tomato', 'Spinach']
print("Length of list : ", len(lst))
print("First Element : ", lst[0])
print("Last Element : ", lst[-1])
lst.append('Ladyfinger')
print("Updated List : ", lst)
lst.remove('Bittergourd')
print("Updated List : ", lst)
lst.sort()
print("Sorted List : ", lst)
lst.pop(1)
print("Updated List : ", lst)
lst.reverse()
print("Reversed List : ", lst)

print("Multiplication on list : ", lst*5)

lst = lst[:4]
print("Sliced List : ", lst)

lst.clear()
print("Cleared List : ", lst)