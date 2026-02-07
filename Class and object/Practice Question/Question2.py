# Write a class calculator capable of finding square cube and squareroot of a number. 

class calculator:
     
    def __init__(self,n):
        self.number = n

    def square(self):
        return self.number * self.number    
    
    def cube(self):
        return self.square() * self.number
    
    def squareroot(self):
        return self.number ** 0.5
    
num = int(input("Enter any nuber : "))    
n = calculator(num)
print(f"The squre cube and squareroot of {num} is {n.square()}, {n.cube()} and {n.squareroot()}")