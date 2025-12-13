import numpy as np
from numpy import random

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1[0])
print(arr1[2:4])
for i in arr1:
    print(i)

arr2 = np.array([[1,2,3,5],[3,4,5,6]])
print(arr2.shape)
print(arr2.reshape(8,1))

arr3 = np.array([1,2,3,4,4])

arr = np.concatenate((arr1, arr3))
print(arr)

x = np.where(arr==4)
print(x)
print(np.sort(arr))

print(random.randint(100))

print(np.arange(3)+1)

student_data_type = [('name', 'S15'), ('class', int), ('height', float)]
student_details = [('Tazkeer', 12, 88.9), ('Nail', 6, 52.5), ('Paul', 9, 67.2), ('Dua', 11, 64.7)]

students = np.array(student_details, dtype=student_data_type)
print("Original Array: ")
print(students)

print("\nSort by height: ")
sorted_students = np.sort(students, order='height')
print(sorted_students)