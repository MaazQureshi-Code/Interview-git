def bubble_sort(arr):
    for i in arr:
        for j in arr:
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j +1] , arr[j]
arr = [5,2,32]
bubble_sort(arr)
print(arr)