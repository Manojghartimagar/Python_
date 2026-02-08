# Write a program to filter a list of numbers which are divisible by 5.

from typing import List
numbers : list[int] = [1,2,8,50,80,35,50,7,68,93,54,60]

def divBy5(n):
    if n%5 ==0:
        return True
    return False

Fivedivisible_Number = filter(divBy5,numbers)
print(list(Fivedivisible_Number))