def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")


def sum(n):
    if (n==0):
        return 0
    return n+sum(n-1)
    
print(f"Sum of {num} is {sum(num)}")