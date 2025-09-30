




def find_missing(arr):
    n = 100
    expected_sum  = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum



arr = list(range(1,101))
arr.remove(57)

print("Missing number:", find_missing(arr))