# Given two lists of numbers of the same length, use map to create a list of their sums element-wise.


l1 = [1,6,-8,10,59]
l2= [4,7,9,20,-70]

print(l1)
print(l2)

def sum(x,y):
    return x+y

sumList = map(sum,l1,l2)
print(list(sumList))
