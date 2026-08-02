num = [5, 2, 4, 6, 1, 3]
def Insertion_Sort(array):
    # we start from the index 1 
    for i in range(1,len(array)):
        # we start from index 1  and  we get the Element as key or temp we compare it to left element 
        temp = array[i]
        # here we get the element we want to compare
        j = i  - 1 
        # here we do the conditional staff
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array
print(Insertion_Sort(num))