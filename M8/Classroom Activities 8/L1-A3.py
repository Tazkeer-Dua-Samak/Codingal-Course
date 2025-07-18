def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'Cat', 'V'], [2, 'Dog', 'V'], [3, 'Bird', 'VI'], [4, 'Insect', 'VI']]

print("\nOriginal list of lists: ")
print(students)
print("\nConverted list to a dictionary")
print(test(students))