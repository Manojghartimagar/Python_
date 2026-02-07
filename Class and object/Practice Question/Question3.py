# Create a class with a class attribute "a" ; create an object from it and set "a" directly using object.a = 0. Does this change the class attribute?

class classA:
     
    def __init__(self,value):
        self.a = value

object = classA(80)
object.a = 0
print(object.a)