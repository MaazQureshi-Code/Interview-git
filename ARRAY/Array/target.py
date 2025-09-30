# Array in Python (list is dynamic but works like array)

# find the target of the array

n = int(input("Enter size of array:"))


arr = []


for i in range(n):
    arr.append(int (input(f"Enter element {i}:")))
    
    
    target = int(input("Enter target: "))
    
    
    found_index = -1
    
    
    for i in range(n):
        if arr[i] == target:
            found_index = i
            break
        

print(found_index)