# write a program using function to find gratest of three numbers.
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))

def greatest_Number(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
    
greatestNum=greatest_Number(num1,num2,num3)
print(f"The greatest number is {greatestNum}")