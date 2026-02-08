# A list contains the multiplication table of 7 write a program to conver it ot a vertical string of same numbers.

l = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Enter any number: "))

multipleList = lambda n:num*n
mul = map(multipleList,l)

for i in list(mul):
    print(i)