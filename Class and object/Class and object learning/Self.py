class student:
    name = input("Enter your name: ")
    level = input("Enter your level: ")

    def getinfo(self):
        print(f"Your name is {self.name} and level is {self.level}")
        
    @staticmethod
    def greet():
        print("Good Morning!")

s = student()
s.name
s.level
s.getinfo()
s.greet()