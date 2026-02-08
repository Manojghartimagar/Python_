#Map Example
l = [1,2,3,4,5,6]
square = lambda x:x*x
sqList = map(square,l)
print(list(sqList))

#Filter Example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

from functools import reduce

#Reduce Example
def sum(a,b):
    return a+b
newList = reduce(sum,l)
print(newList)