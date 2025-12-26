import numpy as np
from numpy import random

arr1 = np.linspace(0, 9, 10, dtype=int) 
'''linspace is used to make sure the elements are 
linearly spaced as was required in the project.
It creates an array of 10 elements'''
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1[0])
print(arr1[2:5])

for i in arr1:
    print(i)

arr2 = arr1.copy()
for i in range(len(arr2)):
    if arr2[i] % 2 != 0:
        arr2[i] = -1

print(arr2)

arr3 = arr1.reshape(2, 5)
print(arr3.shape)
print(arr3)

sum_even = sum(arr1[arr1 % 2 == 0])
print(sum_even)