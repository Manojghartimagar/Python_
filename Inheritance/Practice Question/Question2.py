# Create a class Pets from a class Animal and futher creare class Dog from Pets.Add a method bark to class Dog. 

class Animal:
    def __init__(self):
        print("Animal Class")

    @staticmethod
    def eat():
        print("Eatting food.")

    @staticmethod
    def walk():
        print("Walking in Jungle.")

class Pets(Animal):
    def __init__(self):
        super().__init__()
        print("Pets Class")
        
    @staticmethod
    def lives():
        print("They are lives in homes.")

class Dog(Pets):
    def __init__(self):
        super().__init__()
        print("Dog Class")
    @staticmethod
    def bark():
        print("Dog bark.")

d = Dog()
d.eat()
d.walk()
d.lives()
d.bark()