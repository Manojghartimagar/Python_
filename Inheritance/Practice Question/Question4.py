# Write a class complex to represent complex numbers along with overloaded operators + and * which adds and multiplies them. 

class complex:
    def __init__(self,x,y):
        self.real = x
        self.img =  y

    def display(self):
        print(f"The complex number is {self.real} + {self.img}i")

    def __add__(self,num):
        print("The sum of two complex number is ")
        r = self.real + num.real
        i = self.img + num.img
        return complex(r,i)

    def __mul__(self,num):
        print("The multiplication of two complex number is ")
        r = self.real * num.real - self.img * num.img
        i = self.img * num.real + self.real*num.img
        return complex(r,i)



c1 = complex(1,4)
c2 = complex(12,10)
c1.display()
c2.display()

sum = c1 + c2
sum.display()

multiple = c1 * c2
multiple.display()