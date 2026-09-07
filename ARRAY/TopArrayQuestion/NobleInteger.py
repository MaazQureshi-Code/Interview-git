def NobleInteger(arr):
    arr.sort()
    i = 0
    count = 0
    while i < len(arr):
        currentNum = arr[i]
        for j in range(i + 1 , len(arr)):
            if arr[j] > currentNum:
                count += 1
        if (count >= currentNum):
            return 1
        else: 
            count = 0
            i = i + 1
    return -1

def optimal_Solution(A):
    
    n = len(A)
    A.sort()
    for i in range(n):
        if i < n - 1 and A[i] == A[i + 1]:
            continue
        greater = n - i -1
        if A[i] == greater:
            return 1
    return - 1
print(NobleInteger([6 ,7 , 5]))