my_dict = {}

my_dict = {1: 'apple', 2: 'blueberry'}

my_dict = {'name': 'Jerry', 1: [2, 4, 3]}

my_dict = {'name': 'Tom', 'age': 12}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 21
print(my_dict)

my_dict['address'] = 'Downtown'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address: ", my_dict.get('address'))

my_dict.clear()
print(my_dict)