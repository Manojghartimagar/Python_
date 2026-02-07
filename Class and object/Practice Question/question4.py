# Add a static method in problem 2 to greet the user with hello.

class calculator:
     
    def __init__(self,n):
        self.number = n

    def square(self):
        return self.number * self.number    
    
    def cube(self):
        return self.square() * self.number
    
    def squareroot(self):
        return self.number ** 0.5
    
    @staticmethod
    def greet(name):
        print("Hello! Manoj")
    
name = input("Enter yoiur name : ")
num = int(input("Enter any number : "))    
n = calculator(num)
n.greet(name)
print(f"The squre cube and squareroot of {num} is {n.square()}, {n.cube()} and {n.squareroot()}")
