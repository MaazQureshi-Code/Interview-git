

def array_equal(arr1 , arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if(arr1[i] != arr2[i]):
            return False
    
    return True

array1 = [1,2,3,4]
array2 = [1,2,3,4]

print("Arrays are equal" if array_equal(array1, array2) else "Arrays are not equal")