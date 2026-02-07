class student:
    name = "Manoj"
    Roll_no = 47

    def __init__(self): #dunder method which is automatically called only __init__  (self) is called automatically.
        print("The constructor is formed.")

    def __init__(self,name,roll_no):
        self.name = name
        self.Roll_no = roll_no
    
    @staticmethod
    def greet():
        print("Good Morning!")
    
    def getinfo(self):
        print(f"My name is {self.name} and Rollno is {self.Roll_no}")

s = student()
s.getinfo()

s1 = student("Dipesh",48)
s1.getinfo()