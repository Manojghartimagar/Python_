class student:
    a = 1

    @classmethod #used to show only class attribute value instead of inatence value (s.a = 45) it use cls inatead of self.
    def show(cls):
        print(f"The class value is {cls.a}")

    @property
    def name(self):
        return f"{self.fname},{self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]   #string.split(" ") to gives list[string[0],string[1],...,string[n]]

s = student()
s.a = 45
s.name = "Manoj Gharti"    #To set name method directly in class. 
print(s.fname,s.lname)
s.show()