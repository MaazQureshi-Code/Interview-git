
def sort01(arr):
    """
    Sorts a binary array (containing only 0s and 1s) in-place.
    
    Parameters:
    arr (list): A list of integers containing only 0s and 1s.
    
    Returns:
    None: The input list is sorted in-place.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
            
    
    