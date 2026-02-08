# write a list comprehension to print a list which contaims the multiplication table of a user enterd number.

from typing import List
number: List[int] = [1,2,3,4,5,6,7,8,9,10]
try:
    num = int(input("Enter any number: "))
except ValueError as e:
    print(e)
else:
    print(number)
    multiplication_list: list[int] =[ num*i for i in number ]
    print(multiplication_list)