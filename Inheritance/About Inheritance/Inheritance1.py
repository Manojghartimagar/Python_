class Employee:
    company = "ICT"
    name ="manoj"
    salary = "INR3000"

    def show(self):
        print(f"The name of employee is {self.name} and the salary is {self.salary}")

class programmer(Employee): 
    company = "ICT tech"
    
    def showlanguage(self):
        print(f"The name of programmiing language is {self.language}")

e = Employee()
p = programmer()

e.show()
p.show()