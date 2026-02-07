'''
#singale Inheritance
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

c = Child()
c.show()
c.display()


#Multiple Inheritance
class Father:
    def fshow(self):
        print("Father class")

class Mother:
    def mshow(self):
        print("Mother class")

class Child(Father, Mother):
    def cshow(self):
        print("Child class")

c = Child()
c.fshow()
c.mshow()


#Multilevel Inheritance

class GrandParent:
    def gshow(self):
        print("Grand Parent")

class Parent(GrandParent):
    def pshow(self):
        print("Parent")

class Child(Parent):
    def cshow(self):
        print("Child")

c = Child()
c.gshow()
c.pshow()
c.cshow()

#Hierarchical Inheritance

class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

#Hybrid Inheritance
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


'''

#singale Inheritance
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

c = Child()
c.show()
c.display()