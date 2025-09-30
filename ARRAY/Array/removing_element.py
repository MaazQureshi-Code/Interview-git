def remove_element(array, element):
    return [el for el in array if el != element]


arr = [1, 2, 3, 4, 5, 3, 6]

print(remove_element(arr, 3))  # Output: [1, 2, 4, 5, 6]