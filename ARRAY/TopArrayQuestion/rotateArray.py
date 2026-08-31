# rotated an array by the b position in here  i will do this tommrow learn it and then do it javascript 
# it is never easy at all
# WOrk hard  
def rotateArray(a, b):
    n = len(a)
    b = b % n # in case b is greater then length of the array
    res = []
    for i in range(n):
        res.append(a[(i + b) % n])
    return res


print(rotateArray([1,2,3,4,5,6],1))