#Create a class (2-D vector) and use it to create another class representing a 3-Dvector.

class TwoD_Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getInfo(self):
        print(f"The co-ordinate of 2D vector is ({self.x},{self.y})")


class ThereD_Vector(TwoD_Vector):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z = z
    def getInfo(self):
        super().getInfo()   #super() method is used to call similar named method in parent class from child class.
        print(f"The co-ordinate of 3D vector is ({self.x},{self.y},{self.z})")

v = ThereD_Vector(2,-5,8)
v.getInfo()