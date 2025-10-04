def rotate_array(arr, K):
    N = len(arr)
    if N == 0:
        return arr
    
    K = K % N  # handle large K
    if K < 0:
        K += N

    # rotate using slicing
    return arr[-K:] + arr[:-K]

# Example
arr = [1, 2, 3, 4, 5]
K = 2
print("Rotated Array:", rotate_array(arr, K))
