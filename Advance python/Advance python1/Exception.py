# try:
#     a = int(input("Enter your age: "))
#     print(a)
#     c = int(input(""))
#     b = int(input(""))
#     print(b/c)

# except ZeroDivisionError as z:
#     print(z)

# except ValueError as v:
#     print("v")
#     print(v)

# except Exception as e:
#     print("e")
#     print(e)
# print("Thank You!")

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
if num2 == 0:
    raise ZeroDivisionError( "Invalid number ,Division by zero erro.")

else:
    print(num1/num2)