#Create a class programmer for storing information of few programmers working at microsoft.

class Programmer:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def getInfo(self):
        print("---- Programmer Details ----")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Salary : {self.salary}")


# Creating objects
p1 = Programmer("Manoj", 22, 50000)
p2 = Programmer("Rita", 24, 60000)

p1.getInfo()
p2.getInfo()
