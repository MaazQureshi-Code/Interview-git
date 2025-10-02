
import heapq

def mergesorted_arrays(arr1,arr2):
    i,j=0,0
    merged_array=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while j<len(arr2):
        merged_array.append(arr2[j])
        j+=1
    return merged_array
    
    
    def merge_with_heap(arr1, arr2):
    # Combine both arrays
     merged = arr1 + arr2
    
    # Convert to heap
    heapq.heapify(merged)
    
    # Extract in sorted order
    result = [heapq.heappop(merged) for _ in range(len(merged))]
    return result