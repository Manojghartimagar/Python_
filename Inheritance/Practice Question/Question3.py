# Create a class Employee and add salary and increent properties to it . 
# Write a method salary after Increament method with a @property decorator with a setter which changes the value of increment based on the salary. 

class Employee:
    def __init__(self,salary,increament):
        self.salary = salary
        self.increment = increament
        

    @property
    def After_Increament_Salary(self):
        return self.salary + self.salary * (self.increment/100)
    
    @After_Increament_Salary.setter
    def After_Increament_Salary(self,value):
        self.increment = ((value - self.salary)/self.salary)*100

e = Employee(45000,5)
print(f"Salary : {e.salary}")
print(f"Increment: {e.increment}%")
print(f"After Increment: {e.After_Increament_Salary}")


e.After_Increament_Salary = 50000
print(f"New Increament: {e.increment}%")
print(f"New salary : {e.After_Increament_Salary}")
