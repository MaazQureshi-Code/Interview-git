
# This is one way to do it 
def OccurenceNum(num):
    num.sort()
    nums = []
    for i in num:
        if  i not in nums:
            nums.append(i)
    count = []    
    
    i = 0
    while i < len(nums):
        counter = 0
        for j in num:
            if nums[i] == j:
                counter += 1
        
        count.append(counter)
        i += 1
    return count 


# This is more optimal way to Do it we use Dictionry here to do it 

def occurenceNum(num):
    count = {}
    for i in num:
        if i in count:
            count[i] += 1
        else:
            count [i] = 1            
    return count





print(occurenceNum([3,2,3,3]))