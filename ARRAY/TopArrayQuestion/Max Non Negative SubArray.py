# I will write this Towmmrow In JS

def Max_SubArray(num):
    sub_array = []
    current = []
    for i in num:
        if i < 0:
            if current:
                sub_array.append(current)
                current = []
        else:
            current.append(i)
    # Add the last group 
    if current:
        sub_array.append(current)
    if not sub_array:
        return []
    max_sum = -1
    best_index = 0
    # Find the subarray with the biggest sum
    for i in range(len(sub_array)):
        current_sum = 0
        for j  in sub_array[i]:
            current_sum += j
        if current_sum > max_sum:
            max_sum = current_sum
            best_index = i
    return sub_array[i]

print(Max_SubArray([1, 2, 5, -7, 2, 3]))