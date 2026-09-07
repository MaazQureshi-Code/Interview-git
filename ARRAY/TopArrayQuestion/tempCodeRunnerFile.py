

def NobleInteger(arr):
    arr.sort()
    i = 0
    while i < len(arr):
        currentNum = arr[i]
        for i in range(i + 1 , len(arr)):
            if arr[i] > currentNum:
                return 1
            
        i = i + 1
    return -1





print(NobleInteger([1,1,1,1]))