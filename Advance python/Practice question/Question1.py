# Write a program to print third, fifth and seventh element from  a list using enumerate function. 

from typing import List

number : list[int] = [1,2,5,6,9,10,20,79,30,67]
for index,iteam in enumerate(number):
    if index in (2,4,6):
        print(number[index])