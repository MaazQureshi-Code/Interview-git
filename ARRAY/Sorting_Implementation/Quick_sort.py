
def quicksort(arr,low,high):
    if low < high:
        pivot_index = partition(arr,low,high)
        quicksort(arr,low,pivot_index-1)
        quicksort(arr,pivot_index+1,high)
        
        
def partition(arr, low , high):
    pivot = arr[low]
    i = low
    for j in range(low + 1 , high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j] , arr[i] # swap the array element with each other
    arr[low] , arr[i] = arr[i] , arr[low]
    
    return i



numbers = [7, 2, 9, 4, 1]
quicksort(numbers, 0, len(numbers) - 1)
print(numbers)