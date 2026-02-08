# Write a program to find the maximum of the number in a list using the reduce function.
from functools import reduce
l = [1,2,3,4,5,6,7,89,10,0,69,39]

def max(a,b):
    if (a>=b):
        return a
    return b

max_number = reduce(max,l)
print(f"The maximum number is {max_number}.")

