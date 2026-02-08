#WALRUS Operator  => The walrus operator in Python is written as := and is officially called the assignment expression operator.It was introduced in Python 3.8.

#The walrus operator assigns a value to a variable AND returns that value in the same expression.

#without WALRUS Operator 
'''
 n = len(name)
 if n > 5:
     print(n)
'''

# With walrus operator

'''
if (n := len(name)) > 5:
    print(n)

'''

age = int(input("Enter your age: "))
if(age >= 18):
    print("You can see the video.")
else:
    print("You can not see the video.")

if(age :=int(input("Enter your age: "))>=18):
    print("You can see the video.")
else:
    print("You can not see the video.")