
class GrandParent:
    def __init__(self):
        print("GrandParent constructor called")

    def gshow(self):
        print("Grand Parent method")


class Parent(GrandParent):
    def __init__(self):
        super().__init__()          # call GrandParent constructor
        print("Parent constructor called")

    def pshow(self):
        print("Parent method")


class Child(Parent):
    def __init__(self):
        super().__init__()          # call Parent constructor
        print("Child constructor called")

    def cshow(self):
        print("Child method")


# Creating object
c = Child()

print()
c.gshow()
c.pshow()
c.cshow()

'''
GrandParent constructor called
Parent constructor called
Child constructor called
Parent constructor called
Child constructor called
Child constructor called

Grand Parent method
Parent method
Child method
'''
#Super method key is used to call the inheritance of grandparent parent and child class inheritance.