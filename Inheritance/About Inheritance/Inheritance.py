class Employee:
    company = "ICT"
    name ="manoj"
    salary = "INR3000"

    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")

class programmer: 
    company = "ICT tech"
    name ="manoj"
    salary = "INR3000"

    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")   #It is deficult to copy from parent class and paste to child class so we introduce inheretance. 

    def showlanguage(self):
        print(f"The name of programmiing language is {self.language}")

e = Employee()
p = programmer()

e.show()
p.show()