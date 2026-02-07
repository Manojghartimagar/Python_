class Student:
    def __init__(self, name="Manoj", roll_no=47):
        self.name = name
        self.Roll_no = roll_no
        print("Constructor is called.")

    @staticmethod
    def greet():
        print("Good Morning!")

    def getinfo(self):
        print(f"My name is {self.name} and Rollno is {self.Roll_no}")


# Using default values
s = Student()
s.getinfo()

# Passing custom values
s1 = Student("Dipesh", 48)
s1.getinfo()

# Static method
Student.greet()
