# Write a program to display a/b where a ans b are integers. iF b = 0, display Infinite by handling the ZeroDivisionError

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))

if b == 0:
    raise ZeroDivisionError ("Infinite Error........")
else:
    print(f"a/b = {a/b}")